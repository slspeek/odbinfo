"""" Test fixtures """
import pickle
from zipfile import ZipFile

from pytest import fixture

from odbinfo.test.resource import EMPTYDB, DEFAULT_TESTDB, FIXTURE_DIR


def load_metadata(processed=False):
    """ Returns Metadata object from the test fixture """
    filename = 'metadata-processed.pickle' if processed else 'metadata.pickle'
    with open(FIXTURE_DIR.format(filename), 'rb') as file:
        meta = pickle.load(file)
    return meta


@fixture(scope="function")
def metadata():
    """ Array of all objects from repository """
    yield load_metadata()


@fixture(scope="function")
def metadata_processed():
    """ Array of all objects from repository """
    yield load_metadata(processed=True)


@fixture(scope="session")
def odbzip():
    " odb file open for reading "
    with ZipFile(DEFAULT_TESTDB, "r") as zipfile:
        yield zipfile


@fixture(scope="session")
def empty_odbzip():
    " odb file open for reading "
    with ZipFile(EMPTYDB, "r") as zipfile:
        yield zipfile

