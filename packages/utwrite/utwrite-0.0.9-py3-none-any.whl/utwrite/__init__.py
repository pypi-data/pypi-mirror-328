r"""

Info
----
This module is responsible for command line execution to create unittest from
docstrings.

Usage
-----
First pip install, then run
```sh
utwrite <python_file_to_generate_unittest_from_docstrings>
```

"""
__author__ = 'pb'

from .auto_generate_test import build
from .examples import example_mod

def main():
    import sys
    from . import auto_generate_test

    mods = sys.argv[1:]
    if mods:
        auto_generate_test.build(*mods)
