""" Defines the main datatypes used """
from dataclasses import dataclass, field

from sql_formatter.core import format_sql

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


@dataclass
class Identifier:
    " Unique id for ooobjects "
    object_type: str
    local_id: str


def get_identifier(dataobject) -> Identifier:
    "returns Identifier for `dataobject`"
    return Identifier(dataobject.__class__.__name__, dataobject.title)


@dataclass
class UseCase:
    " `obj` uses `subject`"
    obj: Identifier
    subject: Identifier
    type: str


@dataclass
class Token:
    "lexer token"
    column: int
    line: int
    text: str
    type: int
    index: int
    hidden: bool
    link: [Identifier] = field(init=False, default_factory=list)


@dataclass
class DatabaseDisplay:
    " Field in TextDocument "
    database: str
    table: str
    tabletype: str
    column: str


@dataclass
class TextDocument:
    " ODT or OTT file metadata "
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
    tokens: [Token] = field(init=False, default_factory=list)
    body_tokens: [Token] = field(init=False, repr=False, default_factory=list)
    calls: [] = field(init=False, default_factory=list)
    strings: [] = field(init=False, repr=False,  default_factory=list)
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
    allowinserts: str
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
class BaseColumn:  # pylint: disable=too-many-instance-attributes
    "https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"
    name: str
    title: str = field(init=False)
    autoincrement: bool
    nullable: object
    tablename: str
    typename: str
    precision: str
    scale: str

    def __post_init__(self):
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
class Column(BaseColumn):  # pylint: disable=too-many-instance-attributes
    """ Column properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Column.html
    """
    description: str
    defaultvalue: str


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
    pylibs: [PythonLibrary]
    documents: [TextDocument]
    use_cases: [UseCase] = field(init=False, default_factory=list)

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
        for lib in self.pylibs:
            result.extend(lib.modules)
        return result
