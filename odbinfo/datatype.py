""" Defines the main datatypes used """
from dataclasses import dataclass
import uno
from sql_formatter.core import format_sql

_ooconst = uno.pyuno.getConstantByName
_SUNNAME = "com.sun.star."
_KEYTYPE = _SUNNAME + "sdbcx.KeyType."
""" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/KeyType.html """
KEYTYPES = {_ooconst(_KEYTYPE + name.upper()): name for name in
            ["Unique", "Foreign", "Primary"]}

_COLUMNVALUE = _SUNNAME + "sdbc.ColumnValue."
" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/ColumnValue.html "
COLUMNVALUES = {_ooconst(_COLUMNVALUE + name.upper()): name for name in
                ["No_Nulls", "Nullable", "Nullable_Unknown"]}
_KEYRULE = _SUNNAME + "sdbc.KeyRule."
" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/KeyRule.html "
KEYRULES = {_ooconst(_KEYRULE + name.upper()): name for name in
            ["Cascade", "Restrict", "Set_Null", "No_Action", "Set_Default"]}


@dataclass
class Query:
    " View properties see:"\
        " www.openoffice.org/api/docs/common/ref/com/sun/star/sdb/"\
        " QueryDefinition.html"
    name: str
    command: str

    def __post_init__(self):
        self.command = format_sql(self.command).replace('\n', "<br/>")\
            .replace(' ', "&nbsp;")


View = Query


@dataclass
class Column:  # pylint: disable=too-many-instance-attributes
    """ Column properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Column.html
    """
    name: str
    defaultvalue: str
    description: str
    autoincrement: bool
    nullable: object
    tablename: str
    typename: str
    precision: str
    scale: str

    def __post_init__(self):
        self.nullable = COLUMNVALUES[self.nullable]


@dataclass
class Key:  # pylint: disable=too-many-instance-attributes
    """ Database key properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Key.html
    """
    name: str
    columns: [str]
    relatedcolumns: [str]
    referenced_table: str
    typename: object
    delete_rule: object
    update_rule: object

    def __post_init__(self):
        self.typename = KEYTYPES[self.typename]
        self.update_rule = KEYRULES[self.update_rule]
        self.delete_rule = KEYRULES[self.delete_rule]


@dataclass
class Index:
    """ Index properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Index.html
    """
    name: str
    catalog: str
    unique: bool
    primary: bool
    clustered: bool
    columns: [str]


@dataclass
class Table:
    """ Table properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Table.html
    """
    name: str
    description: str
    keys: [Key]
    columns: [Column]
    indexes: [Index]
