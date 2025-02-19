# from abc import ABC, abstractmethod
from sympy import symbols
from pysatl import Utils
from collections import OrderedDict
from io import BytesIO
from dataclasses import dataclass
from collections.abc import MutableMapping, MutableSequence, MutableSet
import copy
import logging


class NotInitializedError(RuntimeError):
    pass


def ceildiv(a, b):
    return -(a // -b)


def hexdump(buf, offset=0):
    class Hexdump:
        header = 'Offset    00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F\n'

        def __init__(self, buf, off=0):
            if isinstance(buf, str):
                self.buf = buf.encode()
            else:
                self.buf = buf
            self.off = off

        def __iter__(self):
            last_bs, last_line = None, None
            for i in range(0, len(self.buf), 16):
                bs = bytearray(self.buf[i : i + 16])
                line = '{:08x}  {:23}  {:23}  |{:16}|'.format(
                    self.off + i,
                    ' '.join(f'{x:02x}' for x in bs[:8]),
                    ' '.join(f'{x:02x}' for x in bs[8:]),
                    ''.join(chr(x) if 32 <= x < 127 else '.' for x in bs),
                )
                if bs == last_bs:
                    line = '*'
                if bs != last_bs or line != last_line:
                    yield line
                last_bs, last_line = bs, line
            yield f'{self.off + len(self.buf):08x}'

        def __str__(self):
            return Hexdump.header + '\n'.join(self)

        def __repr__(self):
            return Hexdump.header + '\n'.join(self)

    return Hexdump(buf, off=offset).__str__()


def first(s):
    """Return the first element from an ordered collection
    or an arbitrary element from an unordered collection.
    Raise StopIteration if the collection is empty.
    """
    return next(iter(s))


def last(s):
    return next(reversed(s))


def eval_expr(expr, context):
    variables = sorted(expr.free_symbols)
    expr_ctx = {}
    for var in variables:
        var = str(var)
        try:
            val = context[var]
            if val is not None:
                expr_ctx[var] = val
        except KeyError:
            pass
    evaluated = expr.subs(expr_ctx)
    return evaluated


class XCType:

    @property
    def val(self):
        return self._value

    @val.setter
    def val(self, value):
        self._value = value

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    @property
    def offsets(self):
        if self._offsets is None:
            self._compute_offsets()
        return self._offsets

    @property
    def gaps(self):
        if self._gaps is None:
            self._compute_offsets()
        return self._gaps

    @property
    def packed(self):
        return self._packed

    def __init__(self, init=None, *, packed=False):
        self._type_name = None
        self._members = None
        self._value = None
        self._context = None
        self._offsets = None
        self._gaps = None
        self._packed = packed
        if init is not None:
            self.do_init(init)

    def do_init(self, init):
        if init is not None:
            init_bytes = init.to_bytes()
            self.from_bytes(init_bytes)
            self._offsets = None
            self._gaps = None

    def set_member(self, name, value):
        self._members[name.lower()].val = value
        size = self.size()
        if not isinstance(size, int):
            expression = size
            variables = sorted(expression.free_symbols)
            variables = [str(x) for x in variables]
            if name in variables:
                self._offsets = None  # recompute to take the change into account
                self._gaps = None

    def set_member_from_bytes(self, name, dat):
        self._members[name.lower()].from_bytes(dat)
        size = self.size()
        if not isinstance(size, int):
            expression = size
            variables = sorted(expression.free_symbols)
            variables = [str(x) for x in variables]
            if name in variables:
                self._offsets = None  # recompute to take the change into account
                self._gaps = None

    def __str__(self):
        return self.to_str(deep=False)

    def __repr__(self):
        return self.to_str(deep=False)

    def to_str(self, *, deep=False, indent='', skip_long_data=False):
        if self._value is not None:
            # primitive type with concrete value
            return f'{indent}{self._value:#0{self.size()*2+2}x}'
        if self._members is None:
            # primitive type without concrete value
            return indent + self._type_name
        # struct
        out = f'{indent}{self._type_name} ({self.size_str()})\n'

        # return the value of each member
        indent += '  '
        for name in self._members:
            m = self._members[name]
            if deep:
                m_str = m.to_str(deep=True, indent=indent)
                out += f'{indent}{name}: {m_str}'
            else:
                out += f'{indent}{name}: {m._type_name} ({m.size_str()})'
                if m.is_initialized():
                    if m.is_primitive():
                        out += f' = {m}'
                    else:
                        out += f' = {Utils.hexstr(m.to_bytes(),skip_long_data=skip_long_data)}'
            out += '\n'
        return out

    @dataclass
    class VisitorState:
        parent: str = ''
        offset: int = 0
        offset_width: int = 0
        bit_offset: int = 0

    def _compute_offsets(self, *, state=None):
        top_level = state is None
        out = {}
        gaps = {}

        if top_level:
            state = self.VisitorState()
        else:
            state.parent += '.'

        if self.is_primitive() or self.is_array():
            pass  # nothing to do
        else:
            # struct
            # return the offset of each member
            for name in self._members:
                m = self._members[name]
                m._context = copy.deepcopy(self._context)
                full_name = f'{state.parent}{name}'
                if not m.has_bit_granularity():
                    if state.bit_offset > 0:
                        state.bit_offset = 0
                        state.offset += 1
                    if not self.packed:
                        alignement = m.alignement()
                        misalignement = state.offset % alignement
                        if misalignement > 0:
                            gap_size = alignement - misalignement
                            gaps[full_name] = gap_size
                            state.offset += alignement - misalignement
                out[full_name] = state.offset, state.bit_offset
                if not self.is_primitive() and not self.is_array():
                    o = {}
                    g = copy.deepcopy(m.gaps)
                    for item in m.offsets.items():
                        key = f'{state.parent}{name}.{item[0]}'
                        val = item[1][0] + state.offset, item[1][1] + state.bit_offset
                        o[key] = val
                    out = out | o
                    gaps = gaps | g
                if m.has_bit_granularity():
                    total_bit_size = m.bit_size()
                    full_bytes, bits = divmod(total_bit_size, 8)
                    state.offset += full_bytes
                    state.bit_offset += bits
                else:
                    state.offset += m.size()
                if self._context is not None and self._members[name]._value is not None:
                    self._context[name] = self._members[name]._value
        if top_level:
            self._offsets = out
            self._gaps = gaps
        return out, gaps

    def offset(self, name):
        return self.offsets[name]

    class AsciidocVisitorState:
        def __init__(self, *, parent: str = '', offset_width: int = 0, offsets: dict = None, gaps: dict = None):
            if offsets is None:
                offsets = {}
            if gaps is None:
                gaps = {}
            self.parent = parent
            self.offset_width = offset_width
            self.offsets = copy.deepcopy(offsets)
            self.offsets[''] = (0, 0)
            self.gaps = gaps

    def to_asciidoc(self, *, deep=False, skip_long_data=True, title=None, values=False, state=None):
        top_level = state is None
        out = ''
        if top_level:
            state = self.AsciidocVisitorState(
                offset_width=2 + ceildiv(self.size().bit_length(), 4), offsets=self.offsets, gaps=self.gaps
            )
            if title is None:
                title = self._type_name
            out += '[%unbreakable]\n'
            out += f'.{title}'
            if values:
                out += """
[cols="<1,<3,<1,<5"]
[options="header",grid="all"]
|=======================
| Offset | Item | Size | Value
"""
            else:
                out += """
[cols="<1,<6,<1,<2"]
[options="header",grid="all"]
|=======================
| Offset | Item | Size | Type
"""
        o = state.offsets[state.parent]
        offset, bit_offset = o
        if state.parent in state.gaps:
            size = state.gaps[state.parent]
            out += f'<| {offset-size:#0{state.offset_width}x} <| - <| {size} <| PADDING\n'
        if self.is_primitive() or self.is_array():
            if self.has_bit_granularity():
                total_bit_size = self.bit_size()
                full_bytes, bits = divmod(total_bit_size, 8)
                out += f'<| {offset:#0{state.offset_width}x}.{bit_offset} <| {state.parent} <| {full_bytes}.{bits} <|'
            else:
                out += f'<| {offset:#0{state.offset_width}x} <| {state.parent} <| {self.size()} <|'
            if values:
                if self._value is None:
                    out += 'undefined'
                else:
                    # primitive type with concrete value
                    if self.is_array():
                        out += self.to_str(skip_long_data=skip_long_data)
                    else:
                        out += f'{self._value:#0{self.size()*2+2}x}'
            else:
                out += f'{self._type_name}'
            out += '\n'
        else:
            # struct
            if len(state.parent) > 0:
                state.parent += '.'
            # return the value of each member
            for name in self._members:
                m = self._members[name]
                if deep:
                    s = copy.deepcopy(state)
                    s.parent = f'{state.parent}{name}'
                    out += m.to_asciidoc(deep=True, skip_long_data=skip_long_data, values=values, state=s)
                else:
                    out += f'<| {state.parent}{name} <| {m.size()} <| '
                    if values:
                        if m.is_initialized():
                            if m.is_primitive() or m.is_array():
                                out += m.to_str(skip_long_data=skip_long_data)
                            else:
                                out += f'{Utils.hexstr(m.to_bytes(),skip_long_data=skip_long_data)}'
                        else:
                            out += 'undefined'
                    else:
                        out += f'{m._type_name}'
                    out += '\n'

        if top_level:
            out += '|=======================\n'
            out += 'Offset and Size use "bytes.bits" notation.\n'
        return out

    def member(self, path: str):
        names = path.split('.')
        m = self
        for name in names:
            m = m._members[name]
        return m

    def size(self, *, full_bytes_only=False):
        # primitive type shall override this
        bit_size = self.bit_size()
        if isinstance(bit_size, int):
            size, extra_bits = divmod(bit_size, 8)
            if extra_bits > 0:
                if full_bytes_only:
                    return 0
                size += 1
        else:
            # if it is an expression, we assume it is a full byte value
            size = bit_size / 8
        return size

    def bit_size(self):
        # primitive type shall override this
        last_path = last(self.offsets)
        last_offset, last_bit_offset = self.offsets[last_path]
        bit_size = self.member(last_path).bit_size()
        return last_offset * 8 + last_bit_offset + bit_size

    def size_str(self):
        size_bytes = self.size(full_bytes_only=True)
        if not isinstance(size_bytes, int) or size_bytes > 0:
            return f'{size_bytes} bytes'
        else:
            return f'{self.bit_size()} bits'

    def has_bit_granularity(self):
        size_bytes = self.size(full_bytes_only=True)
        if not isinstance(size_bytes, int) or size_bytes > 0:
            return False
        return True

    def alignement(self):
        # class with no member shall override this
        return first(self._members.items())[1].alignement()

    @staticmethod
    def is_primitive():
        return False

    @staticmethod
    def is_array():
        return False

    def is_initialized(self):
        try:
            self.to_bytes()
            return True
        except NotInitializedError:
            return False

    def to_bytes(self) -> bytes:
        if self._members is None:
            if self._value is None:
                raise NotInitializedError()
            return self._value.to_bytes(self.size(), byteorder='little')
        out = bytearray()
        for m in self._members.values():
            out += m.to_bytes()
        return out

    def _check_size(self, data: bytes):
        size = self.size()
        if len(data) != size:
            if isinstance(size, int):
                raise RuntimeError(f'size mismatch: {len(data)} vs {size}')

    def from_bytes(self, data: bytes):
        self._check_size(data)
        if self._members is None:
            self._value = int.from_bytes(data, byteorder='little')
        else:
            for name in self._members:
                m = self._members[name]
                offset, bit_offset = self.offsets[name]
                size = m.size()
                dat = data[offset : offset + size]
                # self._members[name].from_bytes(dat)
                self.set_member_from_bytes(name, dat)

    def fill(self, byte_val):
        if byte_val > 0xFF:
            raise OverflowError()
        val = bytearray([byte_val] * self.size())
        self.from_bytes(val)


class BasePrimitive(XCType):
    @property
    def val(self):
        return self._value

    @val.setter
    def val(self, value):
        if int(value) > self._mask:
            raise OverflowError()
        self._value = value & self._mask

    def __add__(self, other):
        # return (self._value + int(other)) & self._mask
        return self.__class__(init=self._value + int(other))

    def __sub__(self, other):
        o = int(other)
        return self.__class__(init=self._value - o)

    def __mul__(self, other):
        return self.__class__(init=self._value * int(other))

    def __matmul__(self, other):
        return NotImplemented

    def __truediv__(self, other):
        return self.__class__(init=self._value / int(other))

    def __floordiv__(self, other):
        return self.__class__(init=self._value // int(other))

    def __mod__(self, other):
        return self.__class__(init=self._value % int(other))

    def __divmod__(self, other):
        return self.__class__(init=self.__floordiv__(other)), self.__class__(init=self.__mod__(other))

    def __pow__(self, other, modulo=None):
        if modulo is None:
            return self.__class__(init=pow(self._value, int(other)))
        else:
            return self.__class__(init=pow(self._value, int(other)) % int(modulo))

    def __lshift__(self, other):
        return self.__class__(init=self._value << int(other))

    def __rshift__(self, other):
        return self.__class__(init=self._value >> int(other))

    def __and__(self, other):
        return self.__class__(init=self._value & int(other))

    def __xor__(self, other):
        return self.__class__(init=self._value ^ int(other))

    def __or__(self, other):
        return self.__class__(init=self._value | int(other))

    def __radd__(self, other):
        # return (self._value + int(other)) & self._mask
        return self.__class__(init=self._value + int(other))

    def __rsub__(self, other):
        o = int(other)
        return self.__class__(init=o - self._value)

    def __rmul__(self, other):
        return self.__class__(init=self._value * int(other))

    def __rmatmul__(self, other):
        return NotImplemented

    def __rtruediv__(self, other):
        return self.__class__(init=int(other) / self._value)

    def __rfloordiv__(self, other):
        return self.__class__(init=int(other) // self._value)

    def __rmod__(self, other):
        return self.__class__(init=int(other) % self._value)

    def __rdivmod__(self, other):
        return self.__class__(init=self.__rfloordiv__(other)), self.__class__(init=self.__rmod__(other))

    def __rpow__(self, other, modulo=None):
        if modulo is None:
            return self.__class__(init=pow(int(other), self._value))
        else:
            return self.__class__(init=pow(int(other), self._value) % int(modulo))

    def __rlshift__(self, other):
        return self.__class__(init=int(other) << self._value)

    def __rrshift__(self, other):
        return self.__class__(init=int(other) >> self._value)

    def __rand__(self, other):
        return self.__class__(init=self._value & int(other))

    def __rxor__(self, other):
        return self.__class__(init=self._value ^ int(other))

    def __ror__(self, other):
        return self.__class__(init=self._value | int(other))

    def __neg__(self):
        return NotImplemented

    def __pos__(self):
        return NotImplemented

    def __abs__(self):
        return self.__class__(init=abs(self._value))

    def __invert__(self):
        return self.__class__(init=~self._value)

    def __int__(self):
        return self._value

    def __index__(self):
        return self._value

    def __init__(self, init=None, size=None, name=None, mask=None, alignement=None):
        super().__init__()
        self._type_size = size
        if mask:
            self._mask = mask
        else:
            self._mask = (1 << (size * 8)) - 1
        if alignement:
            self._alignement = alignement
        else:
            self._alignement = self._type_size
        self._type_name = name
        self._members = None
        if init is not None:
            self.val = int(init)

    def size(self, *, full_bytes_only=False):
        return self._type_size

    def bit_size(self):
        return self._type_size * 8

    def alignement(self):
        return self._alignement

    @staticmethod
    def is_primitive():
        return True


class Bool(BasePrimitive):
    def __init__(self, init=None):
        super().__init__(init=init, size=1, name='bool', mask=1)


class BasePrimitiveSizeInBits(BasePrimitive):
    def size(self, *, full_bytes_only=False):
        if full_bytes_only and 0 != self._type_size % 8:
            # size is not multiple of 8
            return 0
        return ceildiv(self._type_size, 8)

    def bit_size(self):
        return self._type_size


class BitField(BasePrimitiveSizeInBits):
    def __init__(self, init=None, size=1, alignement=None):
        mask = (1 << size) - 1
        if alignement is None:
            alignement = 1 << (ceildiv(size, 8) - 1).bit_length()
        super().__init__(init=init, size=size, name=f'bitfield{size}_t', mask=mask, alignement=alignement)


class U8(BasePrimitive):
    def __init__(self, init=None):
        super().__init__(init=init, size=1, name='uint8_t')


class U16(BasePrimitive):
    def __init__(self, init=None):
        super().__init__(init=init, size=2, name='uint16_t')


class U32(BasePrimitive):
    def __init__(self, init=None):
        super().__init__(init=init, size=4, name='uint32_t')


class U64(BasePrimitive):
    def __init__(self, init=None):
        super().__init__(init=init, size=8, name='uint64_t')


class U128(BasePrimitive):
    def __init__(self, init=None):
        super().__init__(init=init, size=16, name='uint128_t')


def todo():
    # the math functions are most likely wrong for signed types, so we don't support them yet
    class S8(BasePrimitive):
        def __init__(self, init=None):
            super().__init__(init=init, size=1, name='int8_t')

    class S16(BasePrimitive):
        def __init__(self, init=None):
            super().__init__(init=init, size=2, name='int16_t')

    class S32(BasePrimitive):
        def __init__(self, init=None):
            super().__init__(init=init, size=4, name='int32_t')

    class S64(BasePrimitive):
        def __init__(self, init=None):
            super().__init__(init=init, size=8, name='int64_t')

    class S128(BasePrimitive):
        def __init__(self, init=None):
            super().__init__(init=init, size=16, name='int128_t')


class BaseStruct(XCType):
    def __init__(self, init=None, *, packed=False):
        super().__init__(packed=packed)
        self._members = OrderedDict()
        self._context = {}
        self.do_init(init)


class Array(XCType):
    def __init__(self, init=None, elem_class=None, num_elem=None):
        super().__init__()
        self._type_name = f'{elem_class()._type_name}[]'
        self._context = {}
        self._num_elem_int = None
        self._num_elem_sym = None
        if init is not None:
            self.do_init(init)
        else:
            self._elem_class = elem_class
            if isinstance(num_elem, int):
                self._num_elem_int = num_elem
                # self._value = [elem_class() for i in range(num_elem)]
                self._type_name = f'{elem_class()._type_name}[{self._num_elem_int}]'
            else:
                self._num_elem_sym = num_elem
            if elem_class is None:
                raise RuntimeError('elem_class is mandatory when init is None')

    @staticmethod
    def is_array():
        return True

    def elem_size(self, *, full_bytes_only=False):
        return self._elem_class().size(full_bytes_only=full_bytes_only)  # we support only element types with fixed size

    def elem_bit_size(self):
        return self._elem_class().bit_size()  # we support only element types with fixed size

    def size(self, *, full_bytes_only=False):
        num_elem = self._num_elem_int
        if num_elem is None:
            num_elem = self._num_elem_sym
            try:
                num_elem = eval_expr(num_elem, self._context)
                self._num_elem_int = int(num_elem)
                self._type_name = f'{self._elem_class()._type_name}[{self._num_elem_int}]'
                # self._value = [elem_class() for i in range(num_elem)]
            except Exception as e:
                logging.debug(e)
        return num_elem * self.elem_size()

    def bit_size(self):
        return self.size() * 8

    def alignement(self):
        # class with no member shall override this
        return self._elem_class().alignement()

    def to_bytes(self) -> bytes:
        out = bytearray()
        if self._value is None:
            raise NotInitializedError()
        for m in self._value:
            out += m.to_bytes()
        return out

    def from_bytes(self, data: bytes):
        elem_size = self.elem_size(full_bytes_only=True)
        # if 0 == elem_size:
        #    elem_bit_size = self.elem_bit_size()
        #    TODO ? in C an array of bool takes typically one byte for each bool, so this is not needed

        size = self.size()
        if len(data) != size:
            raise RuntimeError(f'size mismatch: {len(data)} vs {size}')
        data_bytes = BytesIO(data)

        self._value = [self._elem_class() for i in range(self._num_elem_int)]
        for e in self._value:
            e.from_bytes(data_bytes.read(elem_size))

    def to_str(self, *, deep=False, skip_long_data=False, indent=''):
        if self.is_initialized():
            out = indent + '{'
            sep = ''

            def process_elem(e):
                nonlocal out, sep
                out += f'{sep}{e.to_str(deep=deep,skip_long_data=skip_long_data,indent='')}'
                sep = ', '

            if skip_long_data and len(self._value) > 3:
                process_elem(self._value[0])
                out += ', ...'
                process_elem(self._value[-1])
            else:
                for e in self._value:
                    process_elem(e)
            out += '}'
        else:
            num_elem = self._num_elem_int
            if num_elem is None:
                num_elem = self._num_elem_sym
            out = indent + '{' + self._elem_class()._type_name + '}*' + f'{num_elem}'
        return out

    def fill(self, val):
        self._value = [self._elem_class(init=val) for i in range(self._num_elem_int)]


MUTABLES = MutableMapping, MutableSequence, MutableSet  # Mutable containers


def prop_name(name):
    return 'm_' + name.lower()


def storage_name(name):
    return '_member_' + prop_name(name)


def managed_attribute(name):
    """Return a property that stores values under a private non-public name."""

    @property
    def prop(self):
        return self._members[name.lower()]

    @prop.setter
    def prop(self, value):
        # self._members[name.lower()].val = value
        self.set_member(name.lower(), value)

    return prop


def make_struct(classname, *, packed=False, **options):
    """Return a class with the specified attributes implemented as properties."""

    class Class(BaseStruct):
        def __init__(self, init=None):
            """Initialize instance attribute storage name values."""
            super().__init__(packed=packed)
            self._type_name = classname
            for key, value in options.items():
                if isinstance(value, MUTABLES):  # Mutable?
                    value = copy.deepcopy(value)  # Avoid mutable default arg.
                name = key.lower()
                self._members[name] = value
            self.do_init(init)

    for key in options.keys():  # Create class' properties.
        setattr(Class, prop_name(key), managed_attribute(key))

    Class.__name__ = classname
    return Class


def make_array(elem_cls, n_elem=None, classname=None):
    """Return a class with the specified attributes implemented as properties."""

    class Class(Array):
        def __init__(self, init=None, elem_class=elem_cls, num_elem=n_elem):
            """Initialize instance attribute storage name values."""
            super().__init__(elem_class=elem_class, num_elem=num_elem)
            # self._type_name = classname
            self.do_init(init)

    if classname:
        Class.__name__ = classname
    return Class
