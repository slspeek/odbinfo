"""" Test fixtures """
import pickle
from zipfile import ZipFile

from pytest import fixture

from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB, FIXTURE_DIR_TPL


def load_metadata(processed=False, empty=False):
    """ Returns Metadata object from the test fixture """
    postfix = prefix = ""
    if empty:
        prefix = "empty-"
    if processed:
        postfix = "-processed"
    filename = f"{prefix}metadata{postfix}.pickle"
    with open(FIXTURE_DIR_TPL.format(filename), 'rb') as file:
        meta = pickle.load(file)
    return meta


@fixture(scope="function")
def metadata():
    """ Array of all objects from repository """
    yield load_metadata()


@fixture(scope="function")
def empty_metadata():
    """ Array of all objects from repository """
    yield load_metadata(empty=True)


@fixture(scope="function")
def metadata_processed():
    """ Array of all objects from repository """
    yield load_metadata(processed=True)


@fixture(scope="function")
def empty_metadata_processed():
    """ Array of all objects from repository """
    yield load_metadata(processed=True, empty=True)


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
