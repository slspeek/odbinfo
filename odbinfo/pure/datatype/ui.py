" Graphical User Interface datatypes "
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Union, cast

from odbinfo.pure.datatype.base import DataObject, LinkedString
from odbinfo.pure.datatype.tabular import Query


@dataclass
class CommandDriven(DataObject):
    " Has a command and commandtype "
    command: LinkedString
    commandtype: str
    # Only if commandtype == "command"
    embedded_query: Optional[Query] = field(init=False, default=None)


@dataclass
class DatabaseDisplay(DataObject):
    " Field in TextDocument "
    database: str
    table: LinkedString
    tabletype: str
    column: str

    def __post_init__(self) -> None:
        super().__post_init__()
        self.title = f"{self.table.text}.{self.column}"


@dataclass
class TextDocument(DataObject):
    " ODT or OTT file metadata "
    path: str
    fields: List[DatabaseDisplay]

    def children(self) -> Sequence[DataObject]:
        return self.fields


@dataclass
class EventListener:
    " Control eventlistener "
    event: str
    script: str


# pylint: disable=too-many-instance-attributes
@dataclass
class Control(DataObject):
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
class Grid(DataObject):
    " Table view control"
    columns: List[Control]

    def children(self) -> Sequence[DataObject]:
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

    def children(self) -> Sequence[DataObject]:
        return (cast(List[DataObject], self.controls) +
                cast(List[DataObject], self.subforms))


@dataclass
class Form(DataObject):
    " Toplevel form "
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)

    def children(self) -> Sequence[DataObject]:
        return self.subforms


@dataclass
class Report(CommandDriven):
    " Report metadata "
    output_type: str
    formulas: List[str]
