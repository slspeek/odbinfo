""" Tabular like datatypes """
from dataclasses import dataclass, field
from itertools import chain
from typing import List, Union

from sql_formatter.core import format_sql

from odbinfo.pure.datatype.base import NamedNode, Token, User, WebPageWithUses

# www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/KeyType.html
KEYTYPES = {1: "Primary",
            2: "Unique",
            3: "Foreign"}

# www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/ColumnValue.html
COLUMNVALUES = {0: "No_Nulls",
                1: "Nullable",
                2: "Nullable_Unknown"}

# www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/KeyRule.html
KEYRULES = {0: "Cascade",
            1: "Restrict",
            2: "Set_Null",
            3: "No_Action",
            4: "Set_Default"}


# pylint: disable=too-many-instance-attributes


@dataclass
class BaseColumn(NamedNode):
    """https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"""
    autoincrement: bool
    nullable: Union[str, int]
    tablename: str
    typename: str
    precision: str
    scale: str

    def __post_init__(self):
        self.nullable = COLUMNVALUES[self.nullable]


@dataclass
class QueryColumn(BaseColumn):  # pylint: disable=too-many-instance-attributes
    """https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"""
    position: int
    issigned: bool
    writable: bool
    readonly: bool


@dataclass
class QueryBase(NamedNode):
    """ Query properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdb/
        QueryDefinition.html"""
    command: str
    columns: List[QueryColumn] = field(init=False, default_factory=list)

    tokens: List[Token] = field(init=False, default_factory=list)
    table_tokens: List[Token] = field(init=False, default_factory=list)
    literal_values: List[Token] = field(init=False, default_factory=list)

    def __post_init__(self):
        self.command = format_sql(self.command)

    def children(self):
        return chain(self.columns, self.tokens)


@dataclass
class EmbeddedQuery(QueryBase):
    """ Query object embedded in Report, Listbox or SubForm """


@dataclass
class Query(QueryBase, WebPageWithUses):
    """ Query properties """

    def __post_init__(self):
        super().__post_init__()
        self.title = self.name
        # self.command = format_sql(self.command)


@dataclass
class View(Query):
    """ View properties """


@dataclass
class Column(BaseColumn):  # pylint: disable=too-many-instance-attributes
    """ Column properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Column.html
    """
    description: str
    defaultvalue: str


@dataclass
class Key(User, NamedNode):  # pylint: disable=too-many-instance-attributes
    """ Database key properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Key.html
    """
    columns: List[str]
    relatedcolumns: List[str]
    referenced_table: str
    typename: object
    delete_rule: object
    update_rule: object

    def __post_init__(self):
        # super().__post_init__()
        self.typename = KEYTYPES[self.typename]
        self.update_rule = KEYRULES[self.update_rule]
        self.delete_rule = KEYRULES[self.delete_rule]


@dataclass
class Index(NamedNode):
    """ Index properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Index.html
    """
    catalog: str
    unique: bool
    primary: bool
    clustered: bool
    columns: List[str]


@dataclass
class Table(WebPageWithUses):
    """ Table properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Table.html
    """
    description: str
    keys: List[Key]
    columns: List[Column]
    indexes: List[Index]

    def children(self):
        return chain(self.keys, self.indexes, self.columns)


Tabular = Union[Table, View, Query, EmbeddedQuery]
