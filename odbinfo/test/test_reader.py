""" Reader tests """
import json
from os import path
from zipfile import ZipFile

import pytest

from odbinfo.test.resource import DEFAULT_TESTDB
from odbinfo.reader import read_libraries, _reports, _collect_attribute
from odbinfo.reader import _text_documents, read_text_documents


@pytest.fixture(scope="package")
def odbzip():
    " odb file open for reading "
    with ZipFile(DEFAULT_TESTDB, "r") as zipfile:
        yield zipfile


def test_reports(odbzip):  # pylint: disable=redefined-outer-name
    " _reports  "
    info = _reports(odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


def test_libraries(odbzip):  # pylint: disable=redefined-outer-name
    " libraries "
    print(read_libraries(odbzip))


def test_collect_attribute():
    " simple test "
    data = {"elem": {"@foo": "bar"}, "@foo": "foo"}
    assert _collect_attribute(data, "@foo") == ["bar", "foo"]


def test_collect_attribute1():
    " simple test "
    data = {"@foo": "bar"}
    assert _collect_attribute(data, "@foo") == ["bar"]


def test_collect_element():
    " simple test "
    data = {"@foo": "bar", "foo": {}}
    assert _collect_attribute(data, "foo") == [{}]


def test_text_document():
    " find odts "
    assert len(_text_documents(path.dirname(DEFAULT_TESTDB))) == 3


def test_read_text_documents():
    " find odts "
    print(read_text_documents(path.dirname(DEFAULT_TESTDB), "testdb"))
