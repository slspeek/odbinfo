""" Reader tests """
import json
from os import path

import pytest
import xmltodict

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader import (_collect_attribute, _read_listbox, _reports,
                                 _text_documents, read_forms, read_libraries,
                                 read_python_libraries, read_reports,
                                 read_text_documents)
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip
from odbinfo.test.resource import DEFAULT_TESTDB

LISTBOX_VALUELIST = """
<form:listbox form:name="ListBoxValuesRFamliyID" form:control-implementation="ooo:com.sun.star.form.component.ListBox" xml:id="control6" form:id="control6" form:dropdown="true" form:data-field="RFamliyID" form:input-required="true" form:bound-column="1">
<form:properties>
<form:property form:property-name="ControlTypeinMSO" office:value-type="float" office:value="0"/>
<form:property form:property-name="DefaultControl" office:value-type="string" office:string-value="com.sun.star.form.control.ListBox"/>
<form:property form:property-name="MouseWheelBehavior" office:value-type="float" office:value="0"/>
<form:property form:property-name="ObjIDinMSO" office:value-type="float" office:value="65535"/>
<form:list-property form:property-name="TypedItemList" office:value-type="float"/>
</form:properties>
<form:option form:value="1"/>
<form:option form:value="2"/>
<form:option form:value="3"/>
</form:listbox>
"""


def test_read_listbox_valuelist():
    "test listbox with valuelist"
    data = xmltodict.parse(LISTBOX_VALUELIST)["form:listbox"]
    listbox = _read_listbox(data)
    assert listbox.listsourcetype == "valuelist"
    assert listbox.listsource == "1, 2, 3"


@pytest.mark.slow
def test_reports(odbzip):
    " _reports  "
    info = _reports(odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


@pytest.mark.slow
def test_reports_empty(empty_odbzip):
    " _reports  "
    info = _reports(empty_odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


@pytest.mark.slow
def test_libraries_empty(empty_odbzip):
    " no libraries  "
    read_libraries(empty_odbzip)


@pytest.mark.slow
def test_forms_empty(empty_odbzip):
    " no forms  "
    read_forms(empty_odbzip)


@pytest.mark.slow
def test_libraries(odbzip):
    " libraries "
    read_libraries(odbzip)


@pytest.mark.slow
def test_read_reports(odbzip):
    " reports "
    read_reports(odbzip)


@pytest.mark.slow
def test_read_forms(odbzip):
    " forms "
    read_forms(odbzip)


@pytest.mark.slow
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


@pytest.mark.slow
def test_text_document(shared_datadir):
    " find odts "
    directory = (shared_datadir / DEFAULT_TESTDB).parent
    assert len(list(_text_documents(directory))) == 3


@pytest.mark.slow
def test_read_text_documents(shared_datadir):
    " find odts "
    directory = path.dirname(shared_datadir / DEFAULT_TESTDB)

    print(read_text_documents(TextDocumentsConfig("testdb", [directory])))
