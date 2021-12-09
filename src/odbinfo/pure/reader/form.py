"""reading forms"""
from typing import List, Optional, Tuple, Union
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype import (Control, EventListener, Form, Grid, ListBox,
                                   SubForm)
from odbinfo.pure.reader.common import (attr_default, child_elements,
                                        child_elements_by_tagname, document)


def read_form_item(control_elem: Element) -> Union[Control, Grid, ListBox]:
    """ case on the tagName of `column_elem` to read the right component"""
    if control_elem.tagName == "form:grid":
        return read_grid(control_elem)
    if control_elem.tagName == "form:listbox":
        return read_listbox(control_elem)
    return read_control(control_elem)


def read_subforms(office_form_elem: Element) -> List[SubForm]:
    """read the subforms of a form"""
    return [read_subform(form_form_elem) for form_form_elem in
            child_elements_by_tagname(office_form_elem, "form:form")]


def read_subform(form_form_elem: Element):
    """read a SubForm from `form_form_elem` (<form:form>)"""
    controls: List[Union[Control, ListBox, Grid]] = [
        read_form_item(elem) for elem in
        child_elements(form_form_elem)
        if elem.tagName not in ["form:form", "form:properties"]
    ]
    subforms: List[SubForm] = [
        read_subform(elem) for elem in child_elements_by_tagname(form_form_elem, "form:form")
    ]

    return SubForm(form_form_elem.getAttribute("form:name"),
                   form_form_elem.getAttribute("form:command"),
                   attr_default(form_form_elem,
                                "form:command-type", "command"),
                   attr_default(form_form_elem, "form:allow-deletes", "true"),
                   attr_default(form_form_elem, "form:allow-updates", "true"),
                   attr_default(form_form_elem, "form:allow-inserts", "true"),
                   form_form_elem.getAttribute("form:master-fields"),
                   form_form_elem.getAttribute("form:detail-fields"),
                   controls,
                   subforms)


def read_grid(grid_elem: Element) -> Grid:
    """read a tableview from `grid_elem` <form:grid>"""
    controls = list(
        map(read_grid_control, grid_elem.getElementsByTagName("form:column")))
    return Grid(grid_elem.getAttribute("form:name"),
                controls,
                "Grid")


def office_eventlisteners_elem(control_elem: Element) -> Optional[Element]:
    """find <office:event-listeners> under `control_elem`"""
    off_evl_elem = control_elem.getElementsByTagName("office:event-listeners")
    if not off_evl_elem:
        return None
    return off_evl_elem[0]


def read_eventlisteners(control_elem: Element) -> List[EventListener]:
    """reads the <script:event-listener> under <office:event-listeners> under `control_elem`"""
    office_evlis_elem = office_eventlisteners_elem(control_elem)
    if not office_evlis_elem:
        return []

    def read_listener(script_ev_listener: Element):
        return \
            EventListener(script_ev_listener.getAttribute("script:event-name"),
                          script_ev_listener.getAttribute("xlink:href"))

    return [read_listener(elem) for elem in
            office_evlis_elem.getElementsByTagName("script:event-listener")]


def read_control(control_elem) -> Control:
    """returns Control read from `control_elem` (<form:button>, ...) """
    return \
        Control(control_elem.getAttribute("form:name"),
                control_elem.getAttribute("form:id"),
                control_elem.getAttribute("form:data-field"),
                control_elem.getAttribute("form:input-required"),
                control_elem.getAttribute("form:convert-empty-to-null"),
                control_elem.getAttribute("form:label"),
                control_elem.getAttribute("form:for"),
                control_elem.getAttribute("form:control-implementation"),
                read_eventlisteners(control_elem))


def read_listbox(listbox_elem: Element) -> ListBox:
    """returns a ListBox from `listbox_elem` (<form:listbox>)"""
    listsourcetype = attr_default(
        listbox_elem, "form:list-source-type", "valuelist")
    listsource = listbox_elem.getAttribute("form:list-source")
    if listsourcetype == "valuelist":
        options = listbox_elem.getElementsByTagName('form:option')
        listsource = ", ".join(
            map(lambda x: x.getAttribute('form:value'), options))

    return \
        ListBox(listbox_elem.getAttribute("form:name"),
                listbox_elem.getAttribute("form:id"),
                listbox_elem.getAttribute("form:data-field"),
                listbox_elem.getAttribute("form:input-required"),
                listbox_elem.getAttribute("form:convert-empty-to-null"),
                listbox_elem.getAttribute("form:label"),
                listbox_elem.getAttribute("form:for"),
                listbox_elem.getAttribute("form:control-implementation"),
                read_eventlisteners(listbox_elem),
                listbox_elem.getAttribute("form:bound-column"),
                listbox_elem.getAttribute("form:dropdown"),
                listsourcetype,
                listsource
                )


def read_grid_control(column_elem: Element):
    """ reads the grid control from `column_elem`"""
    elem = child_elements(column_elem)[0]
    control = read_control(elem)
    control.name = column_elem.getAttribute("form:name")
    control.label = column_elem.getAttribute("form:label")
    control.type = column_elem.getAttribute("form:control-implementation")
    return control


def forms(odbzip: ZipFile) -> List[Tuple[str, Element]]:
    """ return a tuple with the form name and <office:forms> element """
    forms_elements = document(
        odbzip, "content.xml").getElementsByTagName("db:forms")
    if not forms_elements:
        return []
    forms_elem = forms_elements[0]

    def load_form(form_elem: Element) -> Element:
        relpath = form_elem.getAttribute("xlink:href") + "/content.xml"
        return document(odbzip, relpath).getElementsByTagName("office:forms")[0]

    return \
        [(form_comp.getAttribute("db:name"), load_form(form_comp))
         for form_comp in forms_elem.getElementsByTagName("db:component")]


def read_forms(odbzip):
    """ Reads form metadata from `odbzip` """
    return [Form(name, read_subforms(data)) for name, data in forms(odbzip)]
