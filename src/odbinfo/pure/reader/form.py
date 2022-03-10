"""Reading forms from the odb-zipfile"""
from typing import List, Union
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.ui import (Control, EventListener, Form, Grid,
                                      ListBox, SubForm)
from odbinfo.pure.reader.common import (attr_default, child_elements,
                                        child_elements_by_tagname,
                                        subdocuments_elements)


def create_form_item(
        control_element: Element) -> Union[Control, Grid, ListBox]:
    """ Case on the tagName of `control_elem` to create the right component"""
    if control_element.tagName == "form:grid":
        return create_grid(form_grid_element=control_element)
    if control_element.tagName == "form:listbox":
        return create_listbox(listbox_element=control_element)
    return create_control(control_element=control_element)


def create_subforms(office_form_element: Element) -> List[SubForm]:
    """Creates the subforms of a <office:form> element `office_form_element`"""
    return [
        create_subform(form_form_element)
        for form_form_element in child_elements_by_tagname(
            office_form_element, "form:form")
    ]


def create_subform(form_form_element: Element):
    """Creates a SubForm from `form_form_element` (<form:form>)
    """
    controls: List[Union[Control, ListBox, Grid]] = [
        create_form_item(elem) for elem in child_elements(form_form_element)
        if elem.tagName not in ["form:form", "form:properties"]
    ]
    subforms: List[SubForm] = [
        create_subform(nested_form_from_element)
        for nested_form_from_element in child_elements_by_tagname(
            form_form_element, "form:form")
    ]

    return SubForm(
        name=form_form_element.getAttribute("form:name"),
        cmd=form_form_element.getAttribute("form:command"),
        cmdtype=attr_default(form_form_element, "form:command-type",
                             "command"),
        allowdeletes=attr_default(form_form_element, "form:allow-deletes",
                                  "true"),
        allowupdates=attr_default(form_form_element, "form:allow-updates",
                                  "true"),
        allowinserts=attr_default(form_form_element, "form:allow-inserts",
                                  "true"),
        masterfields=form_form_element.getAttribute("form:master-fields"),
        detailfields=form_form_element.getAttribute("form:detail-fields"),
        controls=controls,
        subforms=subforms)


def create_grid(form_grid_element: Element) -> Grid:
    """Creates a Grid from the <form:grid> `form_grid_element` """
    controls = [
        create_grid_control(elem)
        for elem in form_grid_element.getElementsByTagName("form:column")
    ]
    return Grid(form_grid_element.getAttribute("form:name"), controls, "Grid")


def create_eventlisteners(control_element: Element) -> List[EventListener]:
    """Creates the list of EventListeners from the <script:event-listener>
        elements under <office:event-listeners> under `control_element`
    """
    office_evlis_elems = control_element.getElementsByTagName(
        "office:event-listeners")
    if not office_evlis_elems:
        return []

    return [
        EventListener(elem.getAttribute("script:event-name"),
                      elem.getAttribute("xlink:href")) for elem in
        office_evlis_elems[0].getElementsByTagName("script:event-listener")
    ]


def is_visible(form_properties_element: Element) -> bool:
    """Looks for EnableVisible property amoung the `form_properties_elements`"""

    for prop_element in form_properties_element.getElementsByTagName(
            "form:property"):
        if prop_element.getAttribute("form:property-name") == "EnableVisible":
            if prop_element.getAttribute("office:boolean-value") == "false":
                return False
    return True


def is_control_visible(control_element: Element) -> bool:
    """Looks for EnableVisible property amoung the properties of `control_element` """
    properties_element = control_element.getElementsByTagName(
        "form:properties")
    if properties_element:
        return is_visible(properties_element[0])
    return True


def create_control(control_element: Element) -> Control:
    """Creates a Control read from `control_elem` (<form:button>, ...) """

    return \
        Control(name=control_element.getAttribute("form:name"),
                controlid=control_element.getAttribute("form:id"),
                datafield=control_element.getAttribute("form:data-field"),
                inputrequired=control_element.getAttribute("form:input-required"),
                convertemptytonull=control_element.getAttribute("form:convert-empty-to-null"),
                label=control_element.getAttribute("form:label"),
                formfor=control_element.getAttribute("form:for"),
                type=control_element.getAttribute("form:control-implementation"),
                isvisible=is_control_visible(control_element),
                eventlisteners=create_eventlisteners(control_element))


def create_listbox(listbox_element: Element) -> ListBox:
    """Returns a ListBox from `listbox_element` (<form:listbox>)"""
    listsourcetype = attr_default(listbox_element,
                                  "form:list-source-type",
                                  default_value="valuelist")
    listsource = listbox_element.getAttribute("form:list-source")
    if listsourcetype == "valuelist":
        options = listbox_element.getElementsByTagName('form:option')
        listsource = ", ".join(x.getAttribute('form:value') for x in options)

    return \
        ListBox(name=listbox_element.getAttribute("form:name"),
                controlid=listbox_element.getAttribute("form:id"),
                datafield=listbox_element.getAttribute("form:data-field"),
                inputrequired=listbox_element.getAttribute("form:input-required"),
                convertemptytonull=listbox_element.getAttribute("form:convert-empty-to-null"),
                label=listbox_element.getAttribute("form:label"),
                formfor=listbox_element.getAttribute("form:for"),
                type=listbox_element.getAttribute("form:control-implementation"),
                isvisible=is_control_visible(listbox_element),
                eventlisteners=create_eventlisteners(listbox_element),
                boundcolumn=listbox_element.getAttribute("form:bound-column"),
                dropdown=listbox_element.getAttribute("form:dropdown"),
                listsourcetype=listsourcetype,
                listsource=listsource
                )


def create_grid_control(column_element: Element) -> Control:
    """ Returns the grid control from `column_element` (<form:column>)"""
    elem = child_elements(column_element)[0]
    control = create_control(control_element=elem)
    control.name = column_element.getAttribute("form:name")
    control.label = column_element.getAttribute("form:label")
    control.type = column_element.getAttribute("form:control-implementation")
    return control


def read_forms(odbzip: ZipFile) -> List[Form]:
    """ Reads form metadata from `odbzip` """
    return [
        Form(name, create_subforms(office_forms_element))
        for name, office_forms_element in subdocuments_elements(
            odbzip=odbzip,
            specified_by_tag="db:forms",
            desired_tag="office:forms")
    ]
