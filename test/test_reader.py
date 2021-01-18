""" Reader tests """
import json
from zipfile import ZipFile
from test.resource import DEFAULT_TESTDB
import pytest
from odbinfo.reader import _forms, read_forms, read_libraries


@pytest.fixture(scope="package")
def odbzip():
    " odb file open for reading "
    with ZipFile(DEFAULT_TESTDB, "r") as zipfile:
        yield zipfile


def test_forms(odbzip):  # pylint: disable=redefined-outer-name
    " _forms  "
    info = _forms(odbzip)
    for _, form in info:
        print(json.dumps(form, indent=4))


def test_read_forms(odbzip):  # pylint: disable=redefined-outer-name
    " read_forms  "
    info = read_forms(odbzip)
    for form in info:
        print(form)


def test_libraries(odbzip):  # pylint: disable=redefined-outer-name
    " libraries "
    print(read_libraries(odbzip))
