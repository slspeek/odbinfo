""" Defines the main datatypes used """
from dataclasses import dataclass, field
import uno

_ooconst = uno.pyuno.getConstantByName
_SUNNAME = "com.sun.star.sdbcx."
_KEYTYPE = _SUNNAME + "KeyType."
""" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/KeyType.html """
KEYTYPES = {_ooconst(_KEYTYPE + name.upper()): name for name in
            ["Unique", "Foreign", "Primary"]}

_COLUMNVALUE = "com.sun.star.sdbc.ColumnValue."
" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/ColumnValue.html "
COLUMNVALUES = {_ooconst(_COLUMNVALUE + name.upper()): name for name in
                ["No_Nulls", "Nullable", "Nullable_Unknown"]}


@dataclass
class Column:  # pylint: disable=too-many-instance-attributes
    """ Column properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Column.html
    """
    name: str
    defaultvalue: str
    description: str
    autoincrement: bool
    _nullable: int = field(repr=False)
    nullable: str = field(init=False)
    tablename: str
    typename: str
    precision: str
    scale: str

    def __post_init__(self):
        self.nullable = COLUMNVALUES[self._nullable]


@dataclass
class Key:
    """ Database key properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Key.html
    """
    name: str
    columns: [str]
    referenced_table: str
    _type: int = field(repr=False)
    typename: str = field(init=False)
    delete_rule: int
    update_rule: int

    def __post_init__(self):
        self.typename = KEYTYPES[self._type]


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
