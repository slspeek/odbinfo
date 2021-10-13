""" Reader tests """
import json
import xml
from os import path

import pytest
import xmltodict

from odbinfo.pure.datatype.config import TextDocumentsConfig
from odbinfo.pure.reader import (_collect_attribute, _read_listbox, _reports,
                                 _text_documents, document, forms, read_forms,
                                 read_libraries, read_python_libraries,
                                 read_reports, read_subforms,
                                 read_text_documents)
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip
from odbinfo.test.resource import DEFAULT_TESTDB

# pylint:disable=line-too-long
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


@pytest.mark.slow
def test_document(odbzip):
    doc = document(odbzip, "content.xml")
    # print(doc.toprettyxml())
    assert doc.documentElement.tagName == "office:document-content"


@pytest.mark.slow
def test_forms(odbzip):
    form_elements = forms(odbzip)
    assert len(form_elements) == 9
    print(form_elements[0][1].tagName)


@pytest.mark.slow
def test_read_subforms(odbzip):
    form_elements = forms(odbzip)
    subforms = read_subforms(form_elements[0][1])
    assert len(subforms) == 1
    print(subforms)


RELATED_SUBFORM = """<?xml version="1.0" encoding="UTF-8"?>
<office:forms form:automatic-focus="false" form:apply-design-mode="false" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ooo="http://openoffice.org/2004/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" office:version="1.2">
<form:form form:name="MainForm" form:command="Plant" form:apply-filter="true" form:command-type="table" form:control-implementation="ooo:com.sun.star.form.component.Form" office:target-frame="">
<form:properties>
<form:property form:property-name="PropertyChangeNotificationEnabled" office:value-type="boolean" office:boolean-value="true"/>
<form:property form:property-name="TargetURL" office:value-type="string" office:string-value=""/>
</form:properties>
<form:form form:name="SubForm" form:command="Family" form:apply-filter="true" form:command-type="table" form:control-implementation="ooo:com.sun.star.form.component.Form" office:target-frame="" form:master-fields="&quot;RFamliyID&quot;" form:detail-fields="&quot;FamilyID&quot;">
<form:properties>
 </form:properties>
<form:fixed-text form:name="lblFamilyID" form:control-implementation="ooo:com.sun.star.form.component.FixedText" xml:id="control1" form:id="control1" form:label="FamilyID" form:for="control2"/>
<form:formatted-text form:name="fmtFamilyID" form:control-implementation="ooo:com.sun.star.form.component.FormattedField" xml:id="control2" form:id="control2" form:data-field="FamilyID" form:input-required="true" form:convert-empty-to-null="true" form:min-value="-2147483648" form:max-value="2147483647">
  <form:properties>
 </form:properties>
</form:formatted-text>
<form:fixed-text form:name="lblName" form:control-implementation="ooo:com.sun.star.form.component.FixedText" xml:id="control3" form:id="control3" form:label="Name" form:for="control4"/>
<form:text form:name="txtName" form:control-implementation="ooo:com.sun.star.form.component.TextField" xml:id="control4" form:id="control4" form:data-field="Name" form:input-required="false" form:convert-empty-to-null="true">
  <form:properties>
  </form:properties>
</form:text>
<form:fixed-text form:name="lblDesc" form:control-implementation="ooo:com.sun.star.form.component.FixedText" xml:id="control5" form:id="control5" form:label="Desc" form:for="control6"/>
<form:textarea form:name="txtDesc" form:control-implementation="ooo:com.sun.star.form.component.TextField" xml:id="control6" form:id="control6" form:data-field="Desc" form:input-required="false" form:convert-empty-to-null="true">
  <form:properties>
  </form:properties>
</form:textarea>
</form:form>
<form:fixed-text form:name="lblid" form:control-implementation="ooo:com.sun.star.form.component.FixedText" xml:id="control7" form:id="control7" form:label="id" form:for="control8"/>
<form:formatted-text form:name="fmtid" form:control-implementation="ooo:com.sun.star.form.component.FormattedField" xml:id="control8" form:id="control8" form:data-field="id" form:input-required="true" form:convert-empty-to-null="true">
<form:properties>
</form:properties>
</form:formatted-text>
<form:fixed-text form:name="lblnaam" form:control-implementation="ooo:com.sun.star.form.component.FixedText" xml:id="control9" form:id="control9" form:label="naam" form:for="control10"/>
<form:text form:name="txtnaam" form:control-implementation="ooo:com.sun.star.form.component.TextField" xml:id="control10" form:id="control10" form:data-field="naam" form:input-required="false" form:convert-empty-to-null="true">
<form:properties>
</form:properties>
</form:text>
<form:fixed-text form:name="lblRFamliyID" form:control-implementation="ooo:com.sun.star.form.component.FixedText" xml:id="control11" form:id="control11" form:label="RFamliyID" form:for="control12"/>
<form:formatted-text form:name="fmtRFamliyID" form:control-implementation="ooo:com.sun.star.form.component.FormattedField" xml:id="control12" form:id="control12" form:data-field="RFamliyID" form:input-required="false" form:convert-empty-to-null="true" form:min-value="-2147483648" form:max-value="2147483647">
<form:properties>
</form:properties>
</form:formatted-text>
</form:form>
</office:forms>
"""


def test_read_subform_related_subform():
    doc = xml.dom.minidom.parseString(RELATED_SUBFORM)
    subforms = read_subforms(doc.documentElement)
    assert len(subforms[0].subforms) == 1
    print(subforms)


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
