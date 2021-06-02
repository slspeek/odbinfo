""" Reads the metadata from a running LibreOffice and from the odb file """
import os
from functools import partial
from itertools import starmap
from typing import List
from zipfile import ZipFile

import xmltodict

from odbinfo.pure.datatype import (Control, DatabaseDisplay, EventListener,
                                   Form, Grid, Library, LinkedString, ListBox,
                                   Module, PythonLibrary, PythonModule, Report,
                                   SubForm, TextDocument)


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


def _text_documents(dir_path) -> List[str]:
    docs = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.odt') or file.endswith('.ott'):
                docs.append(root + '/' + str(file))
    return docs


def _database_displays(doc_path) -> List[DatabaseDisplay]:
    def display(data):
        return \
            DatabaseDisplay(
                data["@text:database-name"],
                data["@text:table-name"],
                data["@text:table-type"],
                data["@text:column-name"]
            )
    with ZipFile(doc_path) as file:
        body = _body_elem(file, "content.xml")["office:text"]
        return sum(map(partial(mapiflist, display),
                       _collect_attribute(body, "text:database-display")), [])


def read_text_documents(dir_path, dbname) -> List[TextDocument]:
    " search odt, ott file and look for database-display fields"
    docs = []
    for doc_path in _text_documents(dir_path):
        displays = _database_displays(doc_path)
        displays = list(filter(
            lambda d: d.database == dbname,
            displays
        ))
        if len(displays) > 0:
            docs.append(
                TextDocument(
                    os.path.basename(doc_path),
                    doc_path,
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
                              LinkedString(info["@rpt:command"]),
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


def read_forms(odbzip):
    """ Reads form metadata from `odbzip` """
    return [Form(name, _read_subforms(data)) for name, data in _forms(odbzip)]


def _read_subforms(data) -> List[SubForm]:
    return mapiflist(_read_subform, data["form:form"])


def _read_form_controls(name, value) -> List[Control]:
    if name == "form:form":
        return mapiflist(_read_subform, value)
    if name == "form:grid":
        return mapiflist(_read_grid, value)
    if name == "form:listbox":
        return mapiflist(_read_listbox, value)
    return mapiflist(_read_control, value)


def _read_subform(data):
    controls = sum(
        starmap(_read_form_controls,
                filter(lambda x: x[0].startswith("form:") and
                       not(x[0] == "form:properties") and
                       not(x[0] == "form:form"), data.items())),
        [])
    subforms = []
    if "form:form" in data.keys():
        subforms.extend(mapiflist(_read_subform, data["form:form"]))
    return SubForm(data["@form:name"],
                   data.get("@form:command", ""),
                   data.get("@form:command-type", ""),
                   data.get("@form:allow-deletes", "true"),
                   data.get("@form:allow-updates", "true"),
                   data.get("@form:allow-inserts", "true"),
                   data.get("@form:master-fields", ""),
                   data.get("@form:detail-fields", ""),
                   controls,
                   subforms)


def _read_grid(data):
    gridname = data["@form:name"]
    controls = mapiflist(_read_grid_control, data["form:column"])
    return Grid(gridname, controls)


def _read_eventlisteners(data) -> List[EventListener]:
    def read_listener(oolistn):
        return \
            EventListener(oolistn["@script:event-name"],
                          oolistn["@xlink:href"])
    eventlisteners = []
    if "office:event-listeners" in data.keys():
        data = data["office:event-listeners"]["script:event-listener"]
        eventlisteners.extend(mapiflist(read_listener, data))
    return eventlisteners


def _read_control(data) -> Control:
    return\
        Control(data.get("@form:name", ""),
                data.get("@form:id", ""),
                data.get("@form:data-field", ""),
                data.get("@form:input-required", ""),
                data.get("@form:convert-empty-to-null", ""),
                data.get("@form:label", ""),
                data.get("@form:for", ""),
                data.get("@form:control-implementation", ""),
                _read_eventlisteners(data))


def _read_listbox(data) -> ListBox:
    return\
        ListBox(data.get("@form:name", ""),
                data.get("@form:id", ""),
                data.get("@form:data-field", ""),
                data.get("@form:input-required", ""),
                data.get("@form:conevrtemptytonull", ""),
                data.get("@form:label", ""),
                data.get("@form:for", ""),
                data.get("@form:control-implementation", ""),
                _read_eventlisteners(data),
                data.get("@form:bound-column"),
                data.get("@form:dropdown"),
                data.get("@form:list-source-type"),
                data.get("@form:list-source")
                )


def _read_grid_control(column):
    for elem in column.keys():
        # if elem == "form:properties":
        #     continue
        if elem.startswith("form:"):
            control = _read_control(column[elem])
    control.name = column["@form:name"]
    control.label = column["@form:label"]
    control.type = column["@form:control-implementation"]
    return control


def _office_body(info):
    return info["office:document-content"]["office:body"]


def _forms(odbzip):
    forms = []
    index = _body_elem(odbzip, "content.xml")["office:database"]
    if "db:forms" not in index:
        return forms

    index = index["db:forms"]
    dbcomponent = index["db:component"]

    def form(frm):
        relpath = frm["@xlink:href"] + "/content.xml"
        info = _body_elem(odbzip, relpath)["office:text"]
        info = info["office:forms"]
        return (frm["@db:name"], info)

    forms = mapiflist(form, dbcomponent)
    return forms


def _parse_xml(odbzip, file):
    return xmltodict.parse(odbzip.read(file))
