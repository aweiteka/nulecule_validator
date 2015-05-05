# -*- coding: utf-8 -*-

import json
from jsonschema import Draft4Validator, RefResolver

from nulecule_validator import exceptions, helper, settings

class Validator(object):
    '''Validates a JSON or YAML document (auto-detected by file extension)
    against the Nulecule SPEC'''

    def __init__(self, version=settings.DEFAULT_VERSION):
        self.version = version
        self._schema = helper.get_schema(self.version)
        self._validator = self._construct_validator()

    def _construct_validator(self):
        base_uri = 'file:' + helper.get_base_dir(self.version)
        resolver = RefResolver(base_uri=base_uri, referrer={})
        validator = Draft4Validator(self._schema, resolver=resolver)
        return validator

    def find_errors(self, filename):
        contents = helper.get_file(filename)
        return sorted(self._validator.iter_errors(contents), key=lambda e: e.path)

