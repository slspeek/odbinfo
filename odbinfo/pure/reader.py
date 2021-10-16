""" Reads the metadata from a running LibreOffice and from the odb file """
import os
from functools import partial
from pathlib import Path
from typing import Generator, List, Optional, Tuple, Union, cast
from xml.dom.minidom import Document, Element, Node, parseString
from zipfile import ZipFile

import xmltodict

from odbinfo.pure.datatype import (Control, DatabaseDisplay, EventListener,
                                   Form, Grid, Library, ListBox, Module,
                                   PythonLibrary, PythonModule, Report,
                                   SubForm, TextDocument)
from odbinfo.pure.datatype.config import TextDocumentsConfig


def document(oozip: ZipFile, path: str) -> Document:
    " return dom.Document with contents of `path` in `oozip`"
    return parseString(oozip.read(path))


def child_elements(elem: Element) -> List[Element]:
    " return direct-child-elements of `elem`"
    return \
        [cast(Element, child)
         for child in elem.childNodes if child.nodeType == Node.ELEMENT_NODE]


def child_elements_by_tagname(elem: Element, tagname: str) -> List[Element]:
    " direct-child-elements by tagName"
    return [child for child in child_elements(elem) if child.tagName == tagname]


def mapiflist(function, maybelist):
    """ apply `function` on singletonlist `maybelist`
        if `maybelist` is not a list"""
    if not isinstance(maybelist, list):
        maybelist = [maybelist]
    return list(map(function, maybelist))


def _collect_attribute(data, attribute):

    def collect_attr(info):
        values = []
        if not info:
            return values
        if not hasattr(info, "items"):
            return values
        for key, value in info.items():
            if key == attribute:
                values.append(value)
                continue
            if key.startswith("@"):
                continue
            values.extend(_collect_attribute(value, attribute))
        return values
    return sum(mapiflist(collect_attr, data), [])


def _body_elem(oozip, path):
    content = _parse_xml(oozip, path)
    return _office_body(content)


def _text_documents(dir_path: Path) -> Generator[Path, None, None]:
    return dir_path.glob("**/*.o[dt]t")


def _database_displays(doc_path: Path) -> List[DatabaseDisplay]:
    def _unnumbered_database_displays(doc_path: Path) -> List[DatabaseDisplay]:
        def display(data):
            return \
                DatabaseDisplay(
                    data["@text:column-name"],
                    data["@text:database-name"],
                    data["@text:table-name"],
                    data["@text:table-type"]
                )
        with ZipFile(doc_path) as file:
            body = _body_elem(file, "content.xml")["office:text"]
            return sum(map(partial(mapiflist, display),
                           _collect_attribute(body, "text:database-display")), [])
    displays = _unnumbered_database_displays(doc_path)
    for index, display in zip(range(len(displays)), displays):
        display.index = index
    return displays


def read_text_documents(config: TextDocumentsConfig) -> List[TextDocument]:
    " search odt, ott file and look for database-display fields"
    docs = []
    if config.search_locations:
        for search_loc in config.search_locations:
            for doc_path in _text_documents(Path(search_loc)):
                displays = _database_displays(doc_path)
                displays = list(filter(
                    lambda d: d.database == config.db_registration_id,
                    displays
                ))
                if len(displays) > 0:
                    docs.append(
                        TextDocument(
                            doc_path.stem,
                            doc_path.name,
                            str(doc_path),
                            displays
                        )
                    )
    return docs


def _reports(odbzip):
    index = _body_elem(odbzip, "content.xml")["office:database"]
    if "db:reports" not in index:
        return []
    index = index["db:reports"]
    dbcomponent = index["db:component"]

    def report(rpt):
        relpath = rpt["@xlink:href"] + "/content.xml"
        info = _body_elem(odbzip, relpath)["office:report"]
        return (rpt["@db:name"], info)

    return mapiflist(report, dbcomponent)


def read_reports(odbzip) -> List[Report]:
    " Read reports from odb file "
    reports = []
    for name, info in _reports(odbzip):
        reports.append(Report(name,
                              info["@rpt:command"],
                              info.get("@rpt:command-type", "command"),
                              info.get("@office:mimetype", ""),
                              _read_report_formulas(info))
                       )
    return reports


def _read_report_formulas(info) -> List[str]:
    return _collect_attribute(info, "@rpt:formula")


def _manifest_fileentries(odbzip):
    manifest = _parse_xml(odbzip, "META-INF/manifest.xml")
    return manifest["manifest:manifest"]["manifest:file-entry"]


def read_python_libraries(odbzip):
    " Read python libraries from `odbzip`"
    libraries = []
    for entry in _manifest_fileentries(odbzip):
        fullpath = entry["@manifest:full-path"]
        if fullpath.startswith("Scripts/python")\
                and entry["@manifest:media-type"] == "application/binary":
            libraries.append(
                _read_python_library(odbzip, fullpath)
            )
    return libraries


def _read_python_library(odbzip, fullpath):
    name = os.path.basename(fullpath.rstrip("/"))
    # if name == "python":
    #     name = "DEFAULT"
    modules = []
    for entry in _manifest_fileentries(odbzip):
        entrypath = entry["@manifest:full-path"]
        if entrypath.startswith(fullpath)\
                and entry["@manifest:media-type"] == "":
            modname = os.path.basename(entrypath)
            if fullpath + modname == entrypath:
                modules.append(_read_python_module(odbzip, entrypath, name))
    return PythonLibrary(name, modules)


def _read_python_module(odbzip, fullpath, library):
    return PythonModule(
        os.path.basename(fullpath),
        library,
        odbzip.read(fullpath).decode()
    )


def _has_libraries(odbzip) -> bool:
    for entry in _manifest_fileentries(odbzip):
        if entry["@manifest:full-path"].startswith("Basic"):
            return True
    return False


def read_libraries(odbzip) -> List[Library]:
    " Reads Basic libraries "
    libraries = []
    if _has_libraries(odbzip):
        script_lc = _parse_xml(odbzip, "Basic/script-lc.xml")
        data = script_lc["library:libraries"]["library:library"]
        read_library = partial(_read_library, odbzip)
        libraries.extend(mapiflist(read_library, data))
    return libraries


def _read_library(odbzip, data) -> Library:
    name = data["@library:name"]
    script_lb = _parse_xml(odbzip, f"Basic/{name}/script-lb.xml")
    data = script_lb["library:library"]["library:element"]
    read_module = partial(_read_module, odbzip, name)
    return Library(name, mapiflist(read_module, data))


def _read_module(odbzip, library_name,  data) -> Module:
    name = data["@library:name"]
    data = _parse_xml(odbzip, f"Basic/{library_name}/{name}.xml")
    return Module(name, library_name, data["script:module"]["#text"])


#
# Forms
#

def read_form_item(control_elem: Element) -> Union[Control, Grid]:
    " case on the tagName of `column_elem` to read the right component"
    if control_elem.tagName == "form:grid":
        return read_grid(control_elem)
    if control_elem.tagName == "form:listbox":
        return read_listbox(control_elem)
    return read_control(control_elem)


def read_subforms(office_form_elem: Element) -> List[SubForm]:
    "read the subforms of a form"
    return list(map(read_subform,
                    child_elements_by_tagname(office_form_elem, "form:form")))


def attr_default(elem, attr, def_value):
    "return `def_value` if `elem` has no attribute `attr` else the attribute value"
    value = elem.getAttribute(attr)
    if value == "":
        return def_value
    return value


def read_subform(form_form_elem: Element):
    "read a SubForm from `form_form_elem` (<form:form>)"
    controls: List[Union[Control, Grid]] = [
        read_form_item(elem) for elem in
        child_elements(form_form_elem)
        if not elem.tagName in ["form:form", "form:properties"]
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
    "read a tableview from `grid_elem` <form:grid>"
    controls = list(
        map(read_grid_control, grid_elem.getElementsByTagName("form:column")))
    return Grid(grid_elem.getAttribute("form:name"),
                controls,
                "Grid")


def office_eventlisteners_elem(control_elem: Element) -> Optional[Element]:
    "find <office:event-listeners> under `control_elem`"
    off_evl_elem = control_elem.getElementsByTagName("office:event-listeners")
    if not off_evl_elem:
        return None
    return off_evl_elem[0]


def read_eventlisteners(control_elem: Element) -> List[EventListener]:
    "reads the <script:event-listener> under <office:event-listeners> under `control_elem`"
    office_evlis_elem = office_eventlisteners_elem(control_elem)
    if not office_evlis_elem:
        return []

    def read_listener(script_ev_listener: Element):
        return\
            EventListener(script_ev_listener.getAttribute("script:event-name"),
                          script_ev_listener.getAttribute("xlink:href"))

    return [read_listener(elem) for elem in
            office_evlis_elem.getElementsByTagName("script:event-listener")]


def read_control(control_elem) -> Control:
    "returns Control read from `control_elem` (<form:button>, ...) "
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
    "returns a ListBox from `listbox_elem` (<form:listbox>)"
    listsourcetype = attr_default(
        listbox_elem, "form:list-source-type", "valuelist")
    listsource = listbox_elem.getAttribute("form:list-source")
    if listsourcetype == "valuelist":
        options = listbox_elem.getElementsByTagName('form:option')
        listsource = ", ".join(
            map(lambda x: x.getAttribute('form:value'), options))

    return\
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
    " reads the grid control from `column_elem`"
    elem = child_elements(column_elem)[0]
    control = read_control(elem)
    control.name = column_elem.getAttribute("form:name")
    control.label = column_elem.getAttribute("form:label")
    control.type = column_elem.getAttribute("form:control-implementation")
    return control


def _office_body(info):
    return info["office:document-content"]["office:body"]


def forms(odbzip: ZipFile) -> List[Tuple[str, Element]]:
    " return a tuple with the form name and <office:forms> element "
    xmldoc = document(odbzip, "content.xml")
    forms_elements = xmldoc.documentElement.getElementsByTagName("db:forms")
    if not forms_elements:
        return []
    forms_elem = forms_elements[0]

    def load_form(form_elem: Element) -> Element:
        relpath = form_elem.getAttribute("xlink:href") + "/content.xml"
        form_doc = document(odbzip, relpath)
        return form_doc.documentElement.getElementsByTagName("office:forms")[0]

    return \
        [(form_comp.getAttribute("db:name"), load_form(form_comp))
         for form_comp in forms_elem.getElementsByTagName("db:component")]


def read_forms(odbzip):
    """ Reads form metadata from `odbzip` """
    return [Form(name, read_subforms(data)) for name, data in forms(odbzip)]


def _parse_xml(odbzip, file):
    return xmltodict.parse(odbzip.read(file))
