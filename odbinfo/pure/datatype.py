""" Defines the main datatypes used """
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Union

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
    bookmark: Optional[str] = field(init=False, default=None)


@dataclass
class Token:
    "lexer token"
    column: int
    line: int
    text: str
    type: int
    index: int
    hidden: bool
    link: List[Identifier] = field(init=False, default_factory=list)


@dataclass
class LinkedString:
    " a string referencing a dataobject "
    text: str
    link: Optional[Identifier] = field(init=False, default=None)


@dataclass
class Node:
    " A node in the graph representation "\
        " Super class of the data objects that have a node of their own "
    name: str
    title: str = field(init=False)

    def __post_init__(self) -> None:
        self.title = self.name

    def children(self) -> List['Node']:  # pylint:disable=no-self-use
        " returns a list of child nodes "
        return []


@dataclass
class DataObject(Node):
    " objects with page of their own "


# pylint: disable=too-many-instance-attributes
@dataclass
class BaseColumn(Node):
    "https://www.openhttps://www.openoffice.org/api/docs/"\
        "common/ref/com/sun/star/sdbc/XResultSetMetaData.html"
    name: str
    title: str = field(init=False)
    autoincrement: bool
    nullable: Union[str, int]
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


@dataclass
class CommandDriven(DataObject):
    " Has a command and commandtype "
    command: LinkedString
    commandtype: str
    # Only if commandtype == "command"
    embedded_query: Optional[Query] = field(init=False, default=None)


def get_identifier(dataobject) -> Identifier:
    "returns Identifier for `dataobject`"
    classname = dataobject.__class__.__name__.lower()
    if classname == "query":
        plural = "queries"
    else:
        plural = classname + "s"
    return Identifier(plural,
                      dataobject.title)


@dataclass
class UseCase:
    " `obj` uses `subject`"
    obj: DataObject
    # ref_location: Union[None, Token, LinkedString]
    subject: DataObject
    type: str


@dataclass
class DatabaseDisplay(Node):
    " Field in TextDocument "
    database: str
    table: LinkedString
    tabletype: str
    column: str

    def __post_init__(self) -> None:
        self.title = f"{self.table.text}.{self.column}"


@dataclass
class TextDocument(DataObject):
    " ODT or OTT file metadata "
    path: str
    fields: List[DatabaseDisplay]


@dataclass
class PythonModule(DataObject):
    " Python Module "
    library: str
    source: str

    def __post_init__(self):
        self.title = f"{self.library}.{self.name}"


@dataclass
class PythonLibrary(DataObject):
    " Python library "
    modules: List[PythonModule]


@dataclass
class BasicCall:
    " a function or procedure call in parsed basic code"
    name_token: Token
    module_token: Token


# pylint:disable=too-many-instance-attributes
@dataclass
class BasicFunction(DataObject):
    " Basic sub or function "
    library: str
    module: str
    name_token_index: int = field(init=False)
    tokens: Sequence[Token] = field(init=False, default_factory=list)
    body_tokens: Sequence[Token] = field(
        init=False, repr=False, default_factory=list)
    calls: List[BasicCall] = field(init=False, default_factory=list)
    strings: List[Token] = field(init=False, repr=False,  default_factory=list)
    title: str = field(init=False)

    def __post_init__(self):
        # self.source = tohtml(self.source)
        self.title = f"{self.name}.{self.module}.{self.library}"


@dataclass
class Module(DataObject):
    " Basic module"
    library: str
    source: str
    callables: List[BasicFunction] = field(init=False, default_factory=list)
    title: str = field(init=False)
    tokens: List[Token] = field(init=False, default_factory=list)
    name_indexes: List[int] = field(init=False, default_factory=list)

    def __post_init__(self):
        # self.source = tohtml(self.source)
        self.title = f"{self.name}.{self.library}"


@dataclass
class Library(DataObject):
    " Basic library"
    modules: List[Module]


@dataclass
class EventListener:
    " Control eventlistener "
    event: str
    script: str


@dataclass
class Control(Node):  # pylint: disable=too-many-instance-attributes
    " Form control "
    name: str
    controlid: str
    datafield: str
    inputrequired: bool
    convertemptytonull: bool
    label: str
    formfor: str
    type: str
    eventlisteners: List[EventListener]


@dataclass
class ListBox(Control):
    " ListBox control"
    boundcolumn: int
    dropdown: bool
    listsourcetype: str
    listsource: str


@dataclass
class Grid(Node):
    " Table view control"
    columns: List[Control]


@dataclass
class SubForm(CommandDriven):  # pylint: disable=too-many-instance-attributes
    " Database subform "
    allowdeletes: str
    allowinserts: str
    allowupdates: str
    masterfields: str
    detailfields: str
    controls: List[Union[Control, Grid]]
    subforms: List['SubForm']
    depth: Optional[int] = field(init=False, default=None)


@dataclass
class Form(DataObject):
    " Toplevel form "
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)


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
class Report(CommandDriven):
    " Report metadata "
    output_type: str
    formulas: List[str]


@dataclass
class Key:  # pylint: disable=too-many-instance-attributes
    """ Database key properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Key.html
    """
    name: str
    columns: List[str]
    relatedcolumns: List[str]
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


@dataclass
class Metadata:  # pylint: disable=too-many-instance-attributes
    """ Collector class for all metadata read from the odb-file """
    tables: List[Table]
    views: List[View]
    queries: List[Query]
    forms: List[Form]
    reports: List[Report]
    libraries: List[Library]
    pylibs: List[PythonLibrary]
    documents: List[TextDocument]
    use_cases: List[UseCase] = field(init=False, default_factory=list)

    def basicfunctions(self) -> List[BasicFunction]:
        "collect all callables from libraries"
        result = []
        for lib in self.libraries:
            for module in lib.modules:
                result.extend(module.callables)
        return result

    def modules(self) -> List[Module]:
        "collect all basic modules from libraries"
        result = []
        for lib in self.libraries:
            result.extend(lib.modules)
        return result

    def pymodules(self) -> List[PythonModule]:
        "collect all python modules from libraries"
        result = []
        for lib in self.pylibs:
            result.extend(lib.modules)
        return result

    def subforms(self) -> List[SubForm]:
        " collect all subforms from the forms and subforms "
        def collect_subforms(subform: SubForm) -> List[SubForm]:
            result = [subform]
            result.extend(sum([collect_subforms(sf)
                          for sf in subform.subforms], []))
            return result

        def collect_subforms_from_form(form: Form) -> List[SubForm]:
            return sum([collect_subforms(sf) for sf in form.subforms], [])

        return sum([collect_subforms_from_form(f) for f in self.forms], [])
