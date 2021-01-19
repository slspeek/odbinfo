""" Reader tests """
import json
from zipfile import ZipFile
from test.resource import DEFAULT_TESTDB
import pytest
from odbinfo.reader import read_libraries, _reports, _collect_attribute


@pytest.fixture(scope="package")
def odbzip():
    " odb file open for reading "
    with ZipFile(DEFAULT_TESTDB, "r") as zipfile:
        yield zipfile


def test_reports(odbzip):  # pylint: disable=redefined-outer-name
    " _reports  "
    info = _reports(odbzip)
    for name, form in info:
        print(name, json.dumps(form, indent=4))


def test_libraries(odbzip):  # pylint: disable=redefined-outer-name
    " libraries "
    print(read_libraries(odbzip))


def test_collect_attribute():
    " simple test "
    data = {"elem": {"@foo": "bar"}, "@foo": "foo"}
    assert _collect_attribute(data, "@foo") == ["bar", "foo"]
