""" Reads the metadata from a running LibreOffice and from the odb file """
from zipfile import ZipFile
from functools import partial
import xmltodict
from odbinfo.datatype import Metadata, View, Query, Table, Column, Index, Key
from odbinfo.datatype import Form, SubForm, Control,\
    Grid, ListBox, EventListener,\
    Library, Module
from odbinfo.ooutil import open_connection


def _has_libraries(odbpath) -> bool:
    with ZipFile(odbpath, "r") as odb:
        manifest = _read_from_odb(odb, "META-INF/manifest.xml")
        for entry in manifest["manifest:manifest"]["manifest:file-entry"]:
            if entry["@manifest:full-path"].startswith("Basic"):
                return True
        return False


def read_libraries(odbpath) -> [Library]:
    " Reads Basic libraries "
    libraries = []
    if _has_libraries(odbpath):
        with ZipFile(odbpath, "r") as odb:
            script_lc = _read_from_odb(odb, "Basic/script-lc.xml")
            data = script_lc["library:libraries"]["library:library"]
            if isinstance(data, list):
                libraries = list(map(partial(_read_library, odbpath), data))
            else:
                libraries.append(_read_library(odbpath, data))
    return libraries


def _read_library(odbpath, data) -> Library:
    name = data["@library:name"]
    modules = []
    with ZipFile(odbpath, "r") as odb:
        script_lb = _read_from_odb(odb, f"Basic/{name}/script-lb.xml")
        data = script_lb["library:library"]["library:element"]
        if isinstance(data, list):
            modules = list(map(partial(_read_module, odbpath, name), data))
        else:
            modules.append(_read_module(odbpath, name, data))
    return Library(name, modules)


def _read_module(odbpath, library_name,  data) -> Module:
    name = data["@library:name"]
    with ZipFile(odbpath, "r") as odb:
        data = _read_from_odb(odb, f"Basic/{library_name}/{name}.xml")
        return Module(name, data["script:module"]["#text"])


def read_forms(odbpath):
    """ Reads form metadata from `odbpath` zip """
    forms = []
    for name, data in _forms(odbpath):
        form = Form(name, _read_subforms(data))
        forms.append(form)
    return forms


def _read_subforms(data):
    subforms = []
    data = data["form:form"]
    if isinstance(data, list):
        subforms = list(map(_read_subform, data))
    else:
        subforms.append(_read_subform(data))
    return subforms


def _read_subform(data):
    controls = []
    subformname = data["@form:name"]
    command = data.get("@form:command", "")
    commandtype = data.get("@form:command-type", "")
    for name in data.keys():
        if name == "form:properties":
            continue
        if name == "form:form":
            value = data[name]
            controls.append(_read_subform(value))
        elif name == "form:grid":
            value = data[name]
            controls.append(_read_grid(value))
        elif name == "form:listbox":
            controls.append(_read_listbox(data[name]))
        elif name.startswith("form:"):
            value = data[name]
            if isinstance(value, list):
                controls.append(list(map(_read_control, value)))
            else:
                controls.append(_read_control(value))
    return SubForm(subformname, command, commandtype, controls)


def _read_grid(data):
    gridname = data["@form:name"]
    controls = []
    for column in data["form:column"]:
        controls.append(_read_grid_control(column))

    return Grid(gridname, controls)


def _read_eventlisteners(data) -> [EventListener]:
    def read_listener(oolistn):
        return \
            EventListener(oolistn["@script:event-name"],
                          oolistn["@xlink:href"])
    eventlisteners = []
    if "office:event-listeners" in data.keys():
        data = data["office:event-listeners"]["script:event-listener"]
        if isinstance(data, list):
            eventlisteners.append(
                list(map(read_listener, data)))
        else:
            eventlisteners.append(read_listener(data))
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
        if elem == "form:properties":
            continue
        if elem.startswith("form:"):
            control = _read_control(column[elem])
    control.label = column["@form:label"]
    control.type = column["@form:control-implementation"]
    return control


def _office_body(info):
    return info["office:document-content"]["office:body"]


def _forms(odbpath):
    with ZipFile(odbpath, "r") as odb:
        content = _read_from_odb(odb, "content.xml")
        index = _office_body(content)["office:database"]["db:forms"]
        forms = []
        for frm in index["db:component"]:
            relpath = frm["@xlink:href"] + "/content.xml"
            info = _office_body(_read_from_odb(odb, relpath))["office:text"]
            info = info["office:forms"]
            forms.append((frm["@db:name"], info))
        return forms


def _read_from_odb(odb, file):
    return xmltodict.parse(odb.read(file))


def read_metadata(datasource, odbpath):
    """ reads all metadata """
    with open_connection(datasource) as con:
        return \
            Metadata(read_tables(con),
                     read_views(con),
                     read_queries(datasource),
                     read_forms(odbpath),
                     read_libraries(odbpath))


def read_views(connection) -> [View]:
    """ Reads view metadata from `connection` """
    return [_read_view(ooview) for ooview in connection.Views]


def _read_view(ooview):
    return View(ooview.Name, ooview.Command)


def read_queries(datasource):
    """ Reads query metadata from `datasource` """
    return list(map(_read_query, datasource.QueryDefinitions))


def _read_query(ooquery):
    return Query(ooquery.Name, ooquery.Command)


def read_tables(connection) -> [Table]:
    """ Reads table metadata from `connection` """
    result = []
    # have to filter out Views
    for ootable in [t for t in connection.Tables if t.Type == "TABLE"]:
        result.append(_read_table(ootable))
    return result


def _read_table(ootable) -> Table:
    columns = list(map(_read_column, ootable.Columns))
    keys = list(map(_read_key, ootable.Keys))
    indexes = list(map(_read_index, ootable.Indexes))
    return \
        Table(ootable.Name,
              ootable.Description,
              keys,
              columns,
              indexes)


def _read_column(oocolumn) -> Column:
    return \
        Column(oocolumn.Name,
               oocolumn.DefaultValue,
               oocolumn.HelpText,
               oocolumn.IsAutoIncrement,
               oocolumn.IsNullable,
               oocolumn.TableName,
               oocolumn.TypeName,
               oocolumn.Precision,
               oocolumn.Scale
               )


def _read_key(ookey) -> Key:
    return \
        Key(ookey.Name,
            list(ookey.Columns.ElementNames),
            [col.RelatedColumn for col in ookey.Columns],
            ookey.ReferencedTable,
            ookey.Type,
            ookey.DeleteRule,
            ookey.UpdateRule
            )


def _read_index(ooindex) -> Index:
    return \
        Index(ooindex.Name,
              ooindex.Catalog,
              ooindex.IsUnique,
              ooindex.IsPrimaryKeyIndex,
              ooindex.IsClustered,
              list(ooindex.Columns.ElementNames))
