""" Defines the main datatypes used """
from dataclasses import dataclass, field
import uno
from sql_formatter.core import format_sql

_ooconst = uno.pyuno.getConstantByName


def _consts(ooconst, values):
    return\
        {_ooconst(ooconst + name.upper()): name for name in
            values}


_SUNNAME = "com.sun.star."
_KEYTYPE = _SUNNAME + "sdbcx.KeyType."
""" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/KeyType.html """
KEYTYPES = _consts(_KEYTYPE, ["Unique", "Foreign", "Primary"])

_COLUMNVALUE = _SUNNAME + "sdbc.ColumnValue."
" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/ColumnValue.html "
COLUMNVALUES = _consts(_COLUMNVALUE, ["No_Nulls",
                                      "Nullable",
                                      "Nullable_Unknown"])
_KEYRULE = _SUNNAME + "sdbc.KeyRule."
" www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/KeyRule.html "
KEYRULES = _consts(_KEYRULE, ["Cascade",
                              "Restrict",
                              "Set_Null",
                              "No_Action",
                              "Set_Default"])


def tohtml(code):
    "preserve spaces tabs and newlines"
    return\
        code.replace('\n', "<br/>")\
            .replace(' ', "&nbsp;")\
            .replace('\t', "&nbsp;&nbsp;&nbsp;&nbsp;")


@dataclass
class Token:
    "lexer token"
    column: int
    line: int
    text: str
    type: int


@dataclass
class DatabaseDisplay:
    " Field in TextDocument "
    database: str
    table: str
    tabletype: str
    column: str


@dataclass
class TextDocument:
    " ODT od OTT file metadata "
    name: str
    path: str
    fields: [DatabaseDisplay]


@dataclass
class Report:
    " Report metadata "
    name: str
    command: str
    commandtype: str
    formulas: [str]


@dataclass
class PythonModule:
    " Python Module "
    library: str
    name: str
    source: str
    title: str = field(init=False)

    def __post_init__(self):
        self.title = f"{self.library}.{self.name}"


@dataclass
class PythonLibrary:
    " Python library "
    name: str
    modules: [PythonModule]


# pylint:disable=too-many-instance-attributes
@dataclass
class Callable:
    " Basic sub or function "
    library: str
    module: str
    name: str
    source: str
    tokens: [Token] = field(init=False, default_factory=list)
    body_tokens: [Token] = field(init=False, default_factory=list)
    body_source: str = field(init=False)
    title: str = field(init=False)

    def __post_init__(self):
        # self.source = tohtml(self.source)
        self.title = f"{self.library}.{self.module}.{self.name}"


@dataclass
class Module:
    " Basic module"
    library: str
    name: str
    source: str
    callables: [Callable] = field(init=False, default_factory=list)
    title: str = field(init=False)
    tokens: [Token] = field(init=False, default_factory=list)

    def __post_init__(self):
        # self.source = tohtml(self.source)
        self.title = f"{self.library}.{self.name}"


@dataclass
class Library:
    " Basic library"
    name: str
    modules: [Module]


@dataclass
class EventListener:
    " Control eventlistener "
    event: str
    script: str


@dataclass
class SubForm:  # pylint: disable=too-many-instance-attributes
    " Database subform "
    name: str
    command: str
    commandtype: str
    allowdeletes: str
    allowinsertes: str
    allowupdates: str
    masterfields: str
    detailfields: str
    controls: [object]


@dataclass
class Form:
    " Toplevel form "
    name: str
    subforms: [SubForm]


@dataclass
class Control:  # pylint: disable=too-many-instance-attributes
    " Form control "
    name: str
    controlid: str
    datafield: str
    inputrequired: bool
    convertemptytonull: bool
    label: str
    formfor: str
    type: str
    eventlisteners: [EventListener]


@dataclass
class ListBox(Control):
    " ListBox control"
    boundcolumn: int
    dropdown: bool
    listsourcetype: str
    listsource: str


@dataclass
class Grid:
    " Table view control"
    name: str
    columns: [Control]


@dataclass
class QueryColumn:  # pylint: disable=too-many-instance-attributes
    "https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"
    name: str
    autoincrement: bool
    nullable: object
    tablename: str
    typename: str
    precision: str
    scale: str
    issigned: bool
    writable: bool
    readonly: bool

    def __post_init__(self):
        self.nullable = COLUMNVALUES[self.nullable]


@dataclass
class Query:
    " View properties see:"\
        " www.openoffice.org/api/docs/common/ref/com/sun/star/sdb/"\
        " QueryDefinition.html"
    name: str
    command: str
    columns: [QueryColumn]

    def __post_init__(self):
        self.command = format_sql(self.command)


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


@dataclass
class Metadata:  # pylint: disable=too-many-instance-attributes
    """ Collector class for all metadata read from the odb-file """
    tables: [Table]
    views: [View]
    queries: [Query]
    forms: [Form]
    reports: [Report]
    libraries: [Library]
    pythonlibraries: [PythonLibrary]
    textdocuments: [TextDocument]

    def callables(self) -> [Callable]:
        "collect all callables from libraries"
        result = []
        for lib in self.libraries:
            for module in lib.modules:
                result.extend(module.callables)
        return result

    def modules(self) -> [Module]:
        "collect all basic modules from libraries"
        result = []
        for lib in self.libraries:
            result.extend(lib.modules)
        return result

    def pymodules(self) -> [PythonModule]:
        "collect all python modules from libraries"
        result = []
        for lib in self.pythonlibraries:
            result.extend(lib.modules)
        return result
