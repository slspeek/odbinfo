"""" Test fixtures """
import pickle
from zipfile import ZipFile

from pytest import fixture


def load_metadata(shared_datadir, processed=False, empty=False):
    """ Returns Metadata object from the test fixture """
    postfix = prefix = ""
    if empty:
        prefix = "empty-"
    if processed:
        postfix = "-processed"
    filename = shared_datadir / f"{prefix}metadata{postfix}.pickle"
    with open(filename, 'rb') as file:
        meta = pickle.load(file)
    return meta


@fixture(scope="function")
def metadata(shared_datadir):
    """ Array of all objects from repository """

    yield load_metadata(shared_datadir)


@fixture(scope="function")
def empty_metadata(shared_datadir):
    """ Array of all objects from repository """
    yield load_metadata(shared_datadir, empty=True)


@fixture(scope="function")
def metadata_processed(shared_datadir):
    """ Array of all objects from repository """
    yield load_metadata(shared_datadir, processed=True)


@fixture(scope="function")
def empty_metadata_processed(shared_datadir):
    """ Array of all objects from repository """
    yield load_metadata(shared_datadir, processed=True, empty=True)


@fixture(scope="function")
def odbzip(shared_datadir):
    " odb file open for reading "

    with ZipFile(shared_datadir / "testdb.odb", "r") as zipfile:
        yield zipfile


@fixture(scope="function")
def empty_odbzip(shared_datadir):
    " odb file open for reading "
    with ZipFile(shared_datadir / "emptydb.odb", "r") as zipfile:
        yield zipfile
