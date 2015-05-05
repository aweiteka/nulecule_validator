# Copyright (C) 2015 Tomas Radej <tradej@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
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

