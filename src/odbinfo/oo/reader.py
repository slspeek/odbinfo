""" Reads the metadata from a running LibreOffice and from the odb file """
from pathlib import Path
from typing import List
from zipfile import ZipFile

from odbinfo.oo.ooutil import open_connection
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import (Column, Index, Key, Query,
                                           QueryColumn, QueryPage, Table, View)
from odbinfo.pure.reader import (read_forms, read_libraries,
                                 read_python_libraries, read_reports,
                                 read_text_documents)
from odbinfo.pure.util import timed


@timed("Read metadata", indent=2)
def read_metadata(config: Configuration, datasource, odbpath: Path) -> Metadata:
    """ reads all metadata """
    with open_connection(datasource) as con:
        with ZipFile(odbpath, "r") as odbzip:
            return \
                Metadata(config.name,
                         read_tables(con),
                         read_views(con),
                         read_queries(con, datasource),
                         read_forms(odbzip),
                         read_reports(odbzip),
                         read_libraries(odbzip),
                         read_python_libraries(odbzip),
                         read_text_documents(config.textdocuments))


@timed("Read views", indent=4)
def read_views(connection) -> List[View]:
    """ Reads view metadata from `connection` """
    return [_read_view(connection, ooview) for ooview in connection.Views]


def _read_view(connection, ooview) -> View:
    view = View(ooview.Name, ooview.Command)
    read_query_columns(connection, view)
    return view


@timed("Read queries", indent=4)
def read_queries(connection, datasource) -> List[Query]:
    """ Reads self metadata from `datasource` """
    queries: List[Query] = [Query(ooquery.Name, ooquery.Command) for ooquery in
                            datasource.QueryDefinitions]

    for query in queries:
        read_query_columns(connection, query)
    return queries


def read_query_columns(connection, query: QueryPage) -> None:
    """ read self columns """
    query.columns = _read_query_columns(connection, query.command)


def _read_query_columns(connection, command) -> List[QueryColumn]:
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
            i,
            rsmeta.isSigned(i),
            rsmeta.isWritable(i),
            rsmeta.isReadOnly(i)
        ))
    return cols


@timed("Read tables", indent=4)
def read_tables(connection) -> List[Table]:
    """ Reads table metadata from `connection` """
    result = []
    # have to filter out Views
    for ootable in [t for t in connection.Tables if t.Type == "TABLE"]:
        result.append(_read_table(ootable))
    return result


def _read_table(ootable) -> Table:
    columns = [_read_column(oocolumn) for oocolumn in ootable.Columns]
    keys = [_read_key(ookey) for ookey in ootable.Keys]
    indexes = [_read_index(ooindex) for ooindex in ootable.Indexes]
    return \
        Table(ootable.Name,
              ootable.Description,
              keys,
              columns,
              indexes)


def _read_column(oocolumn) -> Column:
    return \
        Column(oocolumn.Name,
               oocolumn.IsAutoIncrement,
               oocolumn.IsNullable,
               oocolumn.TableName,
               oocolumn.TypeName,
               oocolumn.Precision,
               oocolumn.Scale,
               oocolumn.HelpText,
               oocolumn.DefaultValue
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
