"""" Test fixtures """
import pickle
from zipfile import ZipFile

from pytest import fixture

from odbinfo.test.resource import DEFAULT_TESTDB, FIXTURE_DIR


def load_metadata():
    """ Returns Metadata object from the test fixture """
    with open(FIXTURE_DIR.format('metadata.pickle'), 'rb') as file:
        meta = pickle.load(file)
    return meta


@fixture(scope="session")
def metadata():
    """ Array of all objects from repository """
    yield load_metadata()


@fixture(scope="session")
def odbzip():
    " odb file open for reading "
    with ZipFile(DEFAULT_TESTDB, "r") as zipfile:
        yield zipfile
