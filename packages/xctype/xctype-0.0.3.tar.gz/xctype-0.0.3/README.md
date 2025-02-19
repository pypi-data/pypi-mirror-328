# xctype
Explicit C types for Python

This is a proof of concept / work in progress for now, see [roadmap](#roadmap).

## Installation
````
python3 -m pip install xctype-***.whl
````

## Roadmap

- get_types: return types used in the struct (with deep argument similar to to_str)
- to_asciidoc
    - raw_bytes option: display values as hexstr 
- to_c: generate typedef
- check_offsets_against_c: generate a program to check struct members offsets
- doc: think about how to attach a doc to each member, preferably in a python/sphinx friendly way to leverage IDEs
- replace make_struct by a decorator ?
- think about way for user to add code to the struct to manipulate it / validate it (struct with CRCs for example)
- replace sympy by plain python eval ? allows to size stuff based on other stuff size for example. maybe no point making this more flexible than C...

