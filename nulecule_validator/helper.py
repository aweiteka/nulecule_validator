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

import os
import yaml

from nulecule_validator import exceptions, settings

def _load_markup(filename):
    '''Load YAML into a structure in memory'''
    with open(filename) as fh:
        contents = yaml.load(fh.read())
    return contents

def get_base_dir(version):
    return os.path.join(settings.SCHEMA_DIR, version, '')

def get_schema(version=settings.DEFAULT_VERSION):
    '''Get Schema based on version. Latest by default'''
    path = os.path.join(get_base_dir(version), 'schema.json')
    try:
        return _load_markup(path)
    except FileNotFoundError as e:
        raise exceptions.SchemaError('Can not load schema: ' + str(e))
    except yaml.scanner.ScannerError as e:
        raise exceptions.SchemaError('Schema not valid JSON or YAML: ' + str(e))

def get_file(filename):
    try:
        return _load_markup(filename)
    except FileNotFoundError as e:
        raise exceptions.SchemaError(str(e))
    except yaml.scanner.ScannerError as e:
        msg = 'File "{fn}" not valid JSON or YAML: {err}'.format(fn=filename, err=str(e))
        raise exceptions.SchemaError(msg)
