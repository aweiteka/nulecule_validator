
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
