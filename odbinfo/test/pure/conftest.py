"""" Test fixtures """
import pickle
from pathlib import Path
from zipfile import ZipFile

from pytest import fixture

from odbinfo.test.regression import directory_regression
from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB

__all__ = [
    "directory_regression",
    "fixture_path",
    "metadata",
    "empty_metadata",
    "metadata_loader",
    "empty_metadata_loader",
    "metadata_processed",
    "metadata_processed_loader",
    "empty_metadata_processed_loader",
    "empty_metadata_processed",
    "odbzip"
]


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
def fixture_path(shared_datadir):
    """ fixture directory """

    yield Path(shared_datadir) / "fixtures"


@fixture(scope="function")
def metadata(shared_datadir):
    """ Array of all objects from repository """

    yield load_metadata(shared_datadir)


@fixture(scope="function")
def metadata_loader(shared_datadir):
    """ metadata delayed reader for benchmarking """

    def inner():
        return load_metadata(shared_datadir)

    yield inner


@fixture(scope="function")
def empty_metadata(shared_datadir):
    """ Array of all objects from repository """
    yield load_metadata(shared_datadir, empty=True)


@fixture(scope="function")
def empty_metadata_loader(shared_datadir):
    """ empty metadata delayed reader for benchmarking """

    def inner():
        return load_metadata(shared_datadir, empty=True)

    yield inner


@fixture(scope="function")
def metadata_processed(shared_datadir):
    """ Array of all objects from repository """
    yield load_metadata(shared_datadir, processed=True)


@fixture(scope="function")
def empty_metadata_processed(shared_datadir):
    """ Array of all objects from repository """
    yield load_metadata(shared_datadir, processed=True, empty=True)


@fixture(scope="function")
def metadata_processed_loader(shared_datadir):
    """ Array of all objects from repository """

    def inner():
        return load_metadata(shared_datadir, processed=True)

    yield inner


@fixture(scope="function")
def empty_metadata_processed_loader(shared_datadir):
    """ Array of all objects from repository """

    def inner():
        return load_metadata(shared_datadir, processed=True, empty=True)

    yield inner


@fixture(scope="function")
def odbzip(shared_datadir):
    """ odb file open for reading """

    with ZipFile(shared_datadir / DEFAULT_TESTDB, "r") as zipfile:
        yield zipfile


@fixture(scope="function")
def empty_odbzip(shared_datadir):
    """ odb file open for reading """
    with ZipFile(shared_datadir / EMPTYDB, "r") as zipfile:
        yield zipfile
