" Graphical User Interface datatypes "
from dataclasses import dataclass, field
from typing import List, Optional, Union

from odbinfo.pure.datatype.base import LinkedString, NamedNode, Node, PageOwner
from odbinfo.pure.datatype.tabular import Query


@dataclass
class CommandDriven(PageOwner):
    " Has a command and commandtype "
    command: LinkedString
    commandtype: str
    # Only if commandtype == "command"
    embedded_query: Optional[Query] = field(init=False, default=None)


@dataclass
class DatabaseDisplay(Node):
    " Field in TextDocument "
    database: str
    table: LinkedString
    tabletype: str
    column: str

    def __post_init__(self):
        self.title = f"{self.table.text}.{self.column}"


@dataclass
class TextDocument(PageOwner):
    " ODT or OTT file metadata "
    path: str
    fields: List[DatabaseDisplay]

    def children(self):
        return self.fields


@dataclass
class EventListener(Node):
    " Control eventlistener "
    event: str
    script: str


# pylint: disable=too-many-instance-attributes
@dataclass
class Control(NamedNode):
    " Form control "
    controlid: str
    datafield: str
    inputrequired: bool
    convertemptytonull: bool
    label: str
    formfor: str
    type: str
    eventlisteners: List[EventListener]

    def children(self):
        return self.eventlisteners


@dataclass
class ListBox(Control):
    " ListBox control"
    boundcolumn: int
    dropdown: bool
    listsourcetype: str
    listsource: str


@dataclass
class Grid(NamedNode):
    " Table view control"
    columns: List[Control]

    def children(self):
        return self.columns


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

    def children(self):
        return self.controls + self.subforms


@dataclass
class Form(PageOwner):
    " Toplevel form "
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)

    def children(self):
        return self.subforms


@dataclass
class Report(CommandDriven):
    " Report metadata "
    output_type: str
    formulas: List[str]
