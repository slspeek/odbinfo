""" Reads the metadata from a running LibreOffice and from the odb file """
import os
from functools import partial
from typing import List, Sequence
from zipfile import ZipFile

from odbinfo.oo.ooutil import open_connection
from odbinfo.pure.datatype import (Column, Index, Key, LinkedString, Metadata,
                                   Query, QueryColumn, Report, Table, View)
from odbinfo.pure.reader import (read_forms, read_libraries,
                                 read_python_libraries, read_reports,
                                 read_text_documents)


def read_metadata(datasource, odbpath):
    """ reads all metadata """
    with open_connection(datasource) as con:
        with ZipFile(odbpath, "r") as odbzip:
            dbname, _ = os.path.splitext(os.path.basename(odbpath))
            reports: List[Report] = read_reports(odbzip)
            return \
                Metadata(odbpath,
                         read_tables(con),
                         read_views(con),
                         read_queries(con, datasource, reports),
                         read_forms(odbzip),
                         reports,
                         read_libraries(odbzip),
                         read_python_libraries(odbzip),
                         read_text_documents(os.path.dirname(odbpath), dbname))


def read_views(connection) -> List[View]:
    """ Reads view metadata from `connection` """
    return [_read_view(connection, ooview) for ooview in connection.Views]


def _read_view(connection, ooview) -> View:
    view = View(ooview.Name, ooview.Command)
    read_query_columns(connection, view)
    return view


def extract_queries(reports: Sequence[Report]) -> List[Query]:
    " Make queries from embedded sqlcommands in reports"
    queries: List[Query] = []
    for report in reports:
        if report.commandtype == "command":
            query = Query(f"{report.name}.Command", report.command.text)
            report.embedded_query = query
            queries.append(query)
    return queries


def read_queries(connection, datasource, reports: List[Report]) -> List[Query]:
    """ Reads query metadata from `datasource` """
    embedded_queries: List[Query] = extract_queries(reports)
    queries: List[Query] = [Query(ooquery.Name, ooquery.Command) for ooquery in
                            datasource.QueryDefinitions]

    read_query_func = partial(read_query_columns, connection)
    return list(map(read_query_func, queries + embedded_queries))


def read_query_columns(connection, query: Query) -> Query:
    " read query columns "
    query.columns = _read_query_columns(connection, query.command)
    return query


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
            rsmeta.isSigned(i),
            rsmeta.isWritable(i),
            rsmeta.isReadOnly(i)
        ))
    return cols


def read_tables(connection) -> List[Table]:
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
            LinkedString(ookey.ReferencedTable),
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
