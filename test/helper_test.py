
import os

FIXTURES_PATH = 'fixtures'

def get_fixture(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), FIXTURES_PATH, path))

