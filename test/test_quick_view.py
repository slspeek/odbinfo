""" Quick view for the objects fixture """
import pickle

from test.resource import FIXTURE_DIR, TEST_OUTPUT
import pytest
from pytest import fixture
from odbinfo.writer import make_site


def load_metadata():
    """ Returns Metadata object from the test fixture """
    with open(FIXTURE_DIR.format('metadata.pickle'), 'rb') as file:
        meta = pickle.load(file)
    return meta


@fixture(scope="package")
def metadata():
    """ Array of all objects from repository """
    yield load_metadata()


# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_quick_view(metadata):
    """ Run without database scan """
    name = "testdb"
    outdir = TEST_OUTPUT.format("")
    make_site(outdir, name, metadata)
