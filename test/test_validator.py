
import pytest
import sys
import yaml

from nulecule_validator import Validator, exceptions, helper, settings

from flexmock import flexmock
from test import helper_test

class TestValidator(object):

    @pytest.mark.parametrize('args', [{}, {'version': settings.DEFAULT_VERSION}])
    def test_validator_initialization(self, args):
        Validator(**args)

    def test_find_errors(self):
        v = Validator()
        v.find_errors(helper_test.get_fixture('valid_spec.yaml'))

    def test_find_errors_fails(self):
        v = Validator()
        with pytest.raises(exceptions.SchemaError) as e:
            v.find_errors('foo/bar/baz/')

        assert 'No such file' in str(e)

class TestSchema(object):

    def test_root_elements_required(self):
        flexmock(helper).should_receive('get_file').with_args('foo').and_return({})
        errors = Validator().find_errors('foo')
        messages = [e.message for e in errors]

        assert "'id' is a required property" in messages
        assert "'specversion' is a required property" in messages
        assert "'graph' is a required property" in messages
