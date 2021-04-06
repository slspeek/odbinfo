""" Reads the metadata from a running LibreOffice and from the odb file """
import os
from functools import partial
from zipfile import ZipFile

from odbinfo.oo.ooutil import open_connection
from odbinfo.pure.datatype import (Column, Index, Key, Metadata, Query,
                                   QueryColumn, Table, View)
from odbinfo.pure.reader import (read_forms, read_libraries,
                                 read_python_libraries, read_reports,
                                 read_text_documents)


def read_metadata(datasource, odbpath):
    """ reads all metadata """
    with open_connection(datasource) as con:
        with ZipFile(odbpath, "r") as odbzip:
            dbname, _ = os.path.splitext(
                os.path.basename(odbpath)
            )
            return \
                Metadata(read_tables(con),
                         read_views(con),
                         read_queries(con, datasource),
                         read_forms(odbzip),
                         read_reports(odbzip),
                         read_libraries(odbzip),
                         read_python_libraries(odbzip),
                         read_text_documents(os.path.dirname(odbpath), dbname))


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
