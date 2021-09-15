""" Reader tests """
import json
from os import path

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader import (_collect_attribute, _reports, _text_documents,
                                 read_forms, read_libraries,
                                 read_python_libraries, read_reports,
                                 read_text_documents)
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip
from odbinfo.test.resource import DEFAULT_TESTDB


def test_reports(odbzip):
    " _reports  "
    info = _reports(odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


def test_reports_empty(empty_odbzip):
    " _reports  "
    info = _reports(empty_odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


def test_libraries_empty(empty_odbzip):
    " no libraries  "
    read_libraries(empty_odbzip)


def test_forms_empty(empty_odbzip):
    " no forms  "
    read_forms(empty_odbzip)


def test_libraries(odbzip):
    " libraries "
    read_libraries(odbzip)


def test_read_reports(odbzip):
    " reports "
    read_reports(odbzip)


def test_read_forms(odbzip):
    " forms "
    read_forms(odbzip)


def test_pylibraries(odbzip):
    " libraries "
    libs = read_python_libraries(odbzip)
    # print(libs)
    assert len(libs) == 2
    assert len(libs[0].modules) == 1
    assert len(libs[1].modules) == 1


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


def test_text_document(shared_datadir):
    " find odts "
    directory = (shared_datadir / DEFAULT_TESTDB).parent
    assert len(_text_documents(directory)) == 3


def test_read_text_documents(shared_datadir):
    " find odts "
    directory = path.dirname(shared_datadir / DEFAULT_TESTDB)

    print(read_text_documents(TextDocumentsConfig("testdb", [directory])))
