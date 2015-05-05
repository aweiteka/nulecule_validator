Nulecule Validator
==================

This is a library for validating application spec files according to the
[Nulecule specification](https://github.com/projectatomic/nulecule). This
library can be imported in your project or used as a stand-alone executable
when invoked through ``validate.py``.

To use the validator in your code, import it through ``from nulecule_validator
import Validator``. Initializing the ``Validator`` class can be done with the
(string) argument ``version``, which specifies the version of the spec to
validate against. When initialized without arguments, ``Validator``
automatically selects the latest available version of the spec.

If you run ``validate.py``, the script either returns 0 silently when the file
in question is valid, or exits with 1 and outputs errors one by one into
``STDERR``.


