""" Reads the metadata from a running LibreOffice and from the odb file """
from zipfile import ZipFile
import xmltodict
from odbinfo.datatype import Metadata, View, Query, Table, Column, Index, Key
from odbinfo.datatype import Form, SubForm, Control, Grid
from odbinfo.ooutil import open_connection


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
    command = data.get("@command", "")
    commandtype = data.get("Command-type", "")
    for name in data.keys():
        if name == "form:properties":
            continue
        if name == "form:form":
            value = data[name]
            controls.append(_read_subform(value))
        elif name == "form:grid":
            value = data[name]
            controls.append(_read_grid(value))
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
        for elem in column.keys():
            if elem == "form:properties":
                continue
            if elem.startswith("form:"):
                controls.append(_read_control(column.get(elem)))
    return Grid(gridname, controls)


def _read_control(data):
    return\
        Control(data.get("@form:name", ""),
                data.get("@form:id", ""),
                data.get("@form:data-field", ""),
                data.get("@form:input-required", ""),
                data.get("@form:conevrtemptytonull", ""),
                data.get("@form:label", ""),
                data.get("@form:formfor", ""),
                data.get("@form:control-implementation", ""))


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


def read_metadata(datasource):
    """ reads all metadata """
    with open_connection(datasource) as con:
        return \
            Metadata(read_tables(con),
                     read_views(con),
                     read_queries(datasource))


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
