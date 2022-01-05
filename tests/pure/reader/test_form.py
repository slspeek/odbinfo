""" Reader tests """

import unittest

import pytest

from odbinfo.pure.reader.common import document_element
from odbinfo.pure.reader.form import (forms, is_visible, read_control,
                                      read_eventlisteners, read_forms,
                                      read_grid, read_listbox, read_subforms)
from tests.pure.reader.test_common import OO_NAMESPACES

FORM_PROPERTIES = f"""
<form:properties {OO_NAMESPACES}>
    <form:property form:property-name="ControlTypeinMSO" office:value-type="float"
                   office:value="0"/>
    <form:property form:property-name="DefaultControl" office:value-type="string"
                   office:string-value="com.sun.star.form.control.FormattedField"/>
    <form:property form:property-name="EnableVisible" office:value-type="boolean"
                   office:boolean-value="false"/>
    <form:property form:property-name="MouseWheelBehavior" office:value-type="float"
                   office:value="0"/>
    <form:property form:property-name="ObjIDinMSO" office:value-type="float"
                   office:value="65535"/>
</form:properties>
"""


def test_has_enable_visible():
    element = document_element(FORM_PROPERTIES)
    assert not is_visible(element)


# pylint:disable=line-too-long
OFFICE_EVENT_LISTENERS = f"""
<control>
<office:event-listeners {OO_NAMESPACES} >
    <script:event-listener script:language="ooo:script" script:event-name="form:performaction" xlink:href="vnd.sun.star.script:Library1.Module1.Main?language=Basic&amp;location=document" xlink:type="simple"/>
</office:event-listeners>
</control>
"""


class ReadEventlisteners(unittest.TestCase):

    def setUp(self):
        self.office_evlis_elem = document_element(
            OFFICE_EVENT_LISTENERS)
        self.listeners = read_eventlisteners(self.office_evlis_elem)

    def test_count(self):
        assert len(self.listeners) == 1

    def test_script(self):
        assert self.listeners[0].script == \
            'vnd.sun.star.script:Library1.Module1.Main?language=Basic&location=document'

    def test_event(self):
        assert self.listeners[0].name == 'form:performaction'


# pylint:disable=line-too-long
LISTBOX_VALUELIST = f"""
<form:listbox form:name="ListBoxValuesRFamliyID" form:control-implementation="ooo:com.sun.star.form.component.ListBox" xml:id="control6" form:id="control6" form:dropdown="true" form:data-field="RFamliyID" form:input-required="true" form:bound-column="1" {OO_NAMESPACES}>
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


class ReadListBoxValueList(unittest.TestCase):

    def setUp(self):
        self.listbox_elem = document_element(LISTBOX_VALUELIST)
        self.listbox = read_listbox(self.listbox_elem)

    def test_listbox_name(self):
        assert self.listbox.name == "ListBoxValuesRFamliyID"

    def test_listbox_id(self):
        assert self.listbox.controlid == "control6"

    def test_listbox_data_field(self):
        assert self.listbox.datafield == "RFamliyID"

    def test_listbox_inputrequired(self):
        assert self.listbox.inputrequired == "true"

    def test_listbox_convert_empty_to_null(self):
        assert self.listbox.convertemptytonull == ""

    def test_listbox_label(self):
        assert self.listbox.label == ""

    def test_listbox_for(self):
        assert self.listbox.formfor == ""

    def test_listbox_implementation(self):
        assert self.listbox.type == "ooo:com.sun.star.form.component.ListBox"

    def test_listbox_boundcolumn(self):
        assert self.listbox.boundcolumn == "1"

    def test_listbox_dropdown(self):
        assert self.listbox.dropdown == "true"

    def test_listbox_listsourcetype(self):
        assert self.listbox.listsourcetype == "valuelist"

    def test_listbox_listsource(self):
        assert self.listbox.listsource == "1, 2, 3"


# pylint:disable=line-too-long
BUTTON_ELEMENT = f"""
<form:button form:name="Knop 1" form:control-implementation="ooo:com.sun.star.form.component.CommandButton" xml:id="control7" form:id="control7" form:label="Say hello" office:target-frame="" form:delay-for-repeat="PT0.050000000S" form:image-position="center" {OO_NAMESPACES}>
<form:properties>
<form:property form:property-name="DefaultControl" office:value-type="string" office:string-value="com.sun.star.form.control.CommandButton"/>
</form:properties>
<office:event-listeners>
<script:event-listener script:language="ooo:script" script:event-name="form:performaction" xlink:href="vnd.sun.star.script:Library1.Module1.Main?language=Basic&amp;location=document" xlink:type="simple"/>
</office:event-listeners>
</form:button>
"""


class ReadControlButton(unittest.TestCase):

    def setUp(self):
        self.control_elem = document_element(BUTTON_ELEMENT)
        self.control = read_control(self.control_elem)

    def test_control_name(self):
        assert self.control.name == "Knop 1"

    def test_control_id(self):
        assert self.control.controlid == "control7"

    def test_control_data_field(self):
        assert self.control.datafield == ""

    def test_control_inputrequired(self):
        assert self.control.inputrequired == ""

    def test_control_convert_empty_to_null(self):
        assert self.control.convertemptytonull == ""

    def test_control_label(self):
        assert self.control.label == "Say hello"

    def test_control_for(self):
        assert self.control.formfor == ""

    def test_control_implementation(self):
        assert self.control.type == "ooo:com.sun.star.form.component.CommandButton"

    def test_control_eventlisteners(self):
        assert len(self.control.eventlisteners) == 1


RELATED_SUBFORM = f"""<?xml version="1.0" encoding="UTF-8"?>
<office:forms form:automatic-focus="false" form:apply-design-mode="false" {OO_NAMESPACES} office:version="1.2">
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
    doc = document_element(RELATED_SUBFORM)
    subforms = read_subforms(doc)
    assert len(subforms[0].subforms) == 1
    print(subforms)


# pylint: disable = line-too-long
GRID_ELEMENT = f"""
<form:grid form:name="MainForm_Grid" form:control-implementation="ooo:com.sun.star.form.component.GridControl" xml:id="control1" form:id="control1"  {OO_NAMESPACES}>
<form:properties>
<form:property form:property-name="DefaultControl" office:value-type="string" office:string-value="com.sun.star.form.control.GridControl"/>
</form:properties>
<form:column form:name="id" form:control-implementation="ooo:FormattedField" form:label="id">
<form:formatted-text xml:id="control2" form:id="control2" form:data-field="id" form:input-required="false" form:convert-empty-to-null="true">
<form:properties>
</form:properties>
</form:formatted-text>
</form:column>
<form:column form:name="naam" form:control-implementation="ooo:TextField" form:label="naam">
<form:text xml:id="control3" form:id="control3" form:data-field="naam" form:input-required="false" form:convert-empty-to-null="true">
<form:properties>
</form:properties>
</form:text>
</form:column>
</form:grid>
"""


class ReadGrid(unittest.TestCase):

    def setUp(self):
        self.grid_elem = document_element(GRID_ELEMENT)

    def test_read_grid(self):
        self.grid = read_grid(self.grid_elem)
        assert len(self.grid.columns) == 2


@pytest.mark.slow
def test_forms(odbzip):
    form_elements = forms(odbzip)
    assert len(form_elements) == 9
    print(form_elements[0][1].tagName)


@pytest.mark.slow
def test_forms_empty(empty_odbzip):
    """ no forms  """
    read_forms(empty_odbzip)


@pytest.mark.slow
def test_read_forms(odbzip):
    """ forms """
    read_forms(odbzip)
