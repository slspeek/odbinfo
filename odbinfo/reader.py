""" Reads the metadata from a running LibreOffice and from the odb file """
from zipfile import ZipFile
from functools import partial
import xmltodict
from odbinfo.datatype import Metadata, View, Query, Table, Column, Index, Key
from odbinfo.datatype import Form, SubForm, Control,\
    Grid, ListBox, EventListener,\
    Library, Module, QueryColumn, Report
from odbinfo.ooutil import open_connection


def mapiflist(function, maybelist):
    " apply `function` on `maybelist` if `maybelist` is not a list"
    if not isinstance(maybelist, list):
        maybelist = [maybelist]
    return list(map(function, maybelist))


def _body_elem(oozip, path):
    content = _parse_xml(oozip, path)
    return _office_body(content)


def _reports(odbzip):
    index = _body_elem(odbzip, "content.xml")["office:database"]["db:reports"]
    dbcomponent = index["db:component"]

    def report(rpt):
        relpath = rpt["@xlink:href"] + "/content.xml"
        info = _body_elem(odbzip, relpath)["office:report"]
        return (rpt["@db:name"], info)

    return mapiflist(report, dbcomponent)


def read_reports(odbzip) -> [Report]:
    " Read reports from odb file "
    reports = []
    for name, info in _reports(odbzip):
        reports.append(Report(name,
                              info["@rpt:command"],
                              info["@rpt:command-type"])
                       )
    return reports


def _has_libraries(odbzip) -> bool:
    manifest = _parse_xml(odbzip, "META-INF/manifest.xml")
    for entry in manifest["manifest:manifest"]["manifest:file-entry"]:
        if entry["@manifest:full-path"].startswith("Basic"):
            return True
    return False


def read_libraries(odbzip) -> [Library]:
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
    modules = []
    script_lb = _parse_xml(odbzip, f"Basic/{name}/script-lb.xml")
    data = script_lb["library:library"]["library:element"]
    read_module = partial(_read_module, odbzip, name)
    modules.extend(mapiflist(read_module, data))
    return Library(name, modules)


def _read_module(odbzip, library_name,  data) -> Module:
    name = data["@library:name"]
    data = _parse_xml(odbzip, f"Basic/{library_name}/{name}.xml")
    return Module(name, data["script:module"]["#text"])


def read_forms(odbzip):
    """ Reads form metadata from `odbzip` """
    forms = []
    for name, data in _forms(odbzip):
        form = Form(name, _read_subforms(data))
        forms.append(form)
    return forms


def _read_subforms(data) -> [SubForm]:
    data = data["form:form"]
    return mapiflist(_read_subform, data)


def _read_subform(data):
    controls = []
    subformname = data["@form:name"]
    command = data.get("@form:command", "")
    commandtype = data.get("@form:command-type", "")
    for name in data.keys():
        collected_controls = []
        value = data[name]
        if name == "form:properties":
            continue
        if name == "form:form":
            collected_controls = mapiflist(_read_subform, value)
        elif name == "form:grid":
            collected_controls = mapiflist(_read_grid, value)
        elif name == "form:listbox":
            collected_controls = mapiflist(_read_listbox, value)
        elif name.startswith("form:"):
            collected_controls = mapiflist(_read_control, value)
        controls.extend(collected_controls)
    return SubForm(subformname, command, commandtype, controls)


def _read_grid(data):
    gridname = data["@form:name"]
    controls = mapiflist(_read_grid_control, data["form:column"])
    return Grid(gridname, controls)


def _read_eventlisteners(data) -> [EventListener]:
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
        if elem == "form:properties":
            continue
        if elem.startswith("form:"):
            control = _read_control(column[elem])
    control.name = column["@form:name"]
    control.label = column["@form:label"]
    control.type = column["@form:control-implementation"]
    return control


def _office_body(info):
    return info["office:document-content"]["office:body"]


def _forms(odbzip):
    index = _body_elem(odbzip, "content.xml")["office:database"]["db:forms"]
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


def read_metadata(datasource, odbpath):
    """ reads all metadata """
    with open_connection(datasource) as con:
        with ZipFile(odbpath, "r") as odbzip:
            return \
                Metadata(read_tables(con),
                         read_views(con),
                         read_queries(con, datasource),
                         read_forms(odbzip),
                         read_reports(odbzip),
                         read_libraries(odbzip))


def read_views(connection) -> [View]:
    """ Reads view metadata from `connection` """
    return [_read_view(connection, ooview) for ooview in connection.Views]


def _read_view(connection, ooview):
    return View(ooview.Name,
                ooview.Command,
                _read_query_columns(connection, ooview.Command))


def read_queries(connection, datasource):
    """ Reads query metadata from `datasource` """
    read_query = partial(_read_query, connection)
    return list(map(read_query, datasource.QueryDefinitions))


def _read_query(connection, ooquery):
    return Query(ooquery.Name,
                 ooquery.Command,
                 _read_query_columns(connection, ooquery.Command))


def _read_query_columns(connection, command) -> [QueryColumn]:
    cols = []
    stmt = connection.createStatement()
    resultset = stmt.executeQuery(command)
    rsmeta = resultset.getMetaData()
    for i in range(1, rsmeta.getColumnCount() + 1):
        cols.append(QueryColumn(
            rsmeta.getColumnName(i),
            rsmeta.isAutoIncrement(i),
            rsmeta.isNullable(i),
            rsmeta.getTableName(i),
            rsmeta.getColumnTypeName(i),
            rsmeta.getPrecision(i),
            rsmeta.getScale(i),
            rsmeta.isSigned(i),
            rsmeta.isWritable(i),
            rsmeta.isReadOnly(i)
        ))
    return cols


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
