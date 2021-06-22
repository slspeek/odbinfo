" Tabular like datatypes "
from dataclasses import dataclass, field
from typing import List, Sequence, Union, cast

from sql_formatter.core import format_sql

from odbinfo.pure.datatype.base import DataObject, LinkedString, Token

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
class BaseColumn(DataObject):
    "https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"
    autoincrement: bool
    nullable: Union[str, int]
    tablename: str
    typename: str
    precision: str
    scale: str

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.tablename}.{self.name}"
        self.nullable = COLUMNVALUES[self.nullable]


@dataclass
class QueryColumn(BaseColumn):  # pylint: disable=too-many-instance-attributes
    "https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"
    issigned: bool
    writable: bool
    readonly: bool


@dataclass
class Query(DataObject):
    " Query properties see:"\
        " www.openoffice.org/api/docs/common/ref/com/sun/star/sdb/"\
        " QueryDefinition.html"
    command: str
    columns: List[QueryColumn] = field(init=False, default_factory=list)

    tokens: List[Token] = field(init=False, default_factory=list)
    table_tokens: List[Token] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.command = format_sql(self.command)

    def children(self) -> Sequence[DataObject]:
        return self.columns


@dataclass
class View(Query):
    " View properties "


@dataclass
class Column(BaseColumn):  # pylint: disable=too-many-instance-attributes
    """ Column properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Column.html
    """
    description: str
    defaultvalue: str


@dataclass
class Key(DataObject):  # pylint: disable=too-many-instance-attributes
    """ Database key properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Key.html
    """
    columns: List[str]
    relatedcolumns: List[str]
    referenced_table: LinkedString
    typename: object
    delete_rule: object
    update_rule: object

    def __post_init__(self):
        super().__post_init__()
        self.typename = KEYTYPES[self.typename]
        self.update_rule = KEYRULES[self.update_rule]
        self.delete_rule = KEYRULES[self.delete_rule]


@dataclass
class Index(DataObject):
    """ Index properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Index.html
    """
    catalog: str
    unique: bool
    primary: bool
    clustered: bool
    columns: List[str]


@dataclass
class Table(DataObject):
    """ Table properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Table.html
    """
    description: str
    keys: List[Key]
    columns: List[Column]
    indexes: List[Index]

    def children(self) -> Sequence[DataObject]:
        return cast(List[DataObject], self.keys) + \
            cast(List[DataObject], self.indexes) + \
            cast(List[DataObject], self.columns)
