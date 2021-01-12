""" Reads the metadata from a running LibreOffice and from the odb file """
from odbinfo.datatype import View, Query, Table, Column, Index, Key


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
