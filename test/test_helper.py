
import pytest
import sys
import yaml

from nulecule_validator import helper, exceptions

from flexmock import flexmock
from test import helper_test


class TestHelper(object):

    @pytest.mark.parametrize('filename', ['valid_json.json', 'valid_yaml.yaml'])
    def test_load_markup(self, filename):
        path = helper_test.get_fixture(filename)
        expected = {'graph': {'item1': {'source': 'http://example.com'}}}

        assert helper._load_markup(path) == expected

class TestGetSchema(object):

    @pytest.mark.parametrize('args', [{}, {'version': 'latest'}])
    def test_signature(self, args):
        helper.get_schema(**args)

    @pytest.mark.parametrize(('error', 'msg'), [
        (FileNotFoundError, 'Can not load schema'),
        (yaml.scanner.ScannerError, 'Schema not valid')
    ])
    def test_raises(self, error, msg):
        flexmock(helper).should_receive('_load_markup').and_raise(error('foo'))
        with pytest.raises(exceptions.SchemaError) as e:
            helper.get_schema()

        assert msg in str(e)

