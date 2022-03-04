""" Reader for the tabular objects: Tables, Views and Queries.
    It depends on a LibreOffice connection and datasource,
    so it needs a running LibreOffice instance to run.
"""
from typing import List

from odbinfo.pure.datatype.tabular import (Column, Index, Key, Query,
                                           QueryColumn, Table, View)
from odbinfo.pure.util import timed


def get_query_columns(connection, command: str) -> List[QueryColumn]:
    """ Retrieves the column information for the SQL-`command` from
        the database `connection`
    """
    cols = []
    stmt = connection.createStatement()
    resultset = stmt.executeQuery(command)
    rsmeta = resultset.getMetaData()
    for i in range(1, rsmeta.getColumnCount() + 1):
        cols.append(
            QueryColumn(name=rsmeta.getColumnName(i),
                        autoincrement=rsmeta.isAutoIncrement(i),
                        nullable=rsmeta.isNullable(i),
                        tablename=rsmeta.getTableName(i),
                        typename=rsmeta.getColumnTypeName(i),
                        precision=rsmeta.getPrecision(i),
                        scale=rsmeta.getScale(i),
                        position=i,
                        issigned=rsmeta.isSigned(i),
                        writable=rsmeta.isWritable(i),
                        readonly=rsmeta.isReadOnly(i)))
    return cols


@timed("Read views", indent=4)
def read_views(connection) -> List[View]:
    """ Reads view metadata from `connection` """
    return [
        View(name=ooview.Name,
             command=ooview.Command,
             columns=get_query_columns(connection, ooview.Command))
        for ooview in connection.Views
    ]


@timed("Read queries", indent=4)
def read_queries(connection, datasource) -> List[Query]:
    """ Reads query metadata from `datasource` """
    return [
        Query(name=ooquery.Name,
              command=ooquery.Command,
              columns=get_query_columns(connection, ooquery.Command))
        for ooquery in datasource.QueryDefinitions
    ]


def create_column(oocolumn) -> Column:
    """Creates a Column from the staroffice column object `oocolumn`"""
    return \
        Column(name=oocolumn.Name,
               autoincrement=oocolumn.IsAutoIncrement,
               nullable=oocolumn.IsNullable,
               tablename=oocolumn.TableName,
               typename=oocolumn.TypeName,
               precision=oocolumn.Precision,
               scale=oocolumn.Scale,
               description=oocolumn.HelpText,
               defaultvalue=oocolumn.DefaultValue
               )


def create_key(ookey) -> Key:
    """Creates a Key from the staroffice key object `ookey`"""
    return \
        Key(name=ookey.Name,
            columns=list(ookey.Columns.ElementNames),
            relatedcolumns=[col.RelatedColumn for col in ookey.Columns],
            referenced_table=ookey.ReferencedTable,
            typename=ookey.Type,
            delete_rule=ookey.DeleteRule,
            update_rule=ookey.UpdateRule
            )


def create_index(ooindex) -> Index:
    """ Creates an Index from the staroffice index object `ooindex`"""
    return \
        Index(name=ooindex.Name,
              catalog=ooindex.Catalog,
              unique=ooindex.IsUnique,
              primary=ooindex.IsPrimaryKeyIndex,
              clustered=ooindex.IsClustered,
              columns=list(ooindex.Columns.ElementNames))


def create_table(ootable) -> Table:
    """Creates a Table for the staroffice object `ootable`"""
    columns = [create_column(oocolumn) for oocolumn in ootable.Columns]
    keys = [create_key(ookey) for ookey in ootable.Keys]
    indexes = [create_index(ooindex) for ooindex in ootable.Indexes]
    return \
        Table(name=ootable.Name,
              description=ootable.Description,
              keys=keys,
              columns=columns,
              indexes=indexes)


@timed("Read tables", indent=4)
def read_tables(connection) -> List[Table]:
    """ Reads table metadata from `connection` """
    return [
        create_table(ootable) for ootable in connection.Tables
        if ootable.Type == "TABLE"
    ]
