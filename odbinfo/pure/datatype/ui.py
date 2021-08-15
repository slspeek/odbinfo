" Graphical User Interface datatypes "
from dataclasses import dataclass, field
from typing import List, Optional, Union

from odbinfo.pure.datatype.base import (NamedNode, Node, PageOwner,
                                        TitleFromParents, User)
from odbinfo.pure.datatype.tabular import Query


@dataclass
class Commander(User):
    " Has a command and commandtype "
    command: str
    commandtype: str
    # Only if commandtype == "command"
    embedded_query: Optional[Query] = field(init=False, default=None)


@dataclass
class DatabaseDisplay(User, Node):
    " Field in TextDocument "
    database: str
    table: str
    tabletype: str
    column: str
    index: int = field(init=False)

    def set_title(self):
        " sets a unique title "
        self.title = f"{self.column}.{self.index}.{self.table}.{self.parent.title}"


@dataclass
class TextDocument(PageOwner):
    " ODT or OTT file metadata "
    filename: str
    path: str
    fields: List[DatabaseDisplay]

    def children(self):
        return self.fields

    def users_match(self, username: str) -> bool:
        # could be done better by enumerating all subpaths
        return username in (self.name, self.filename)


@dataclass
class EventListener(Node):
    " Control eventlistener "
    event: str
    script: str

    def set_title(self):
        " sets a unique title "
        self.title = f"{self.parent.title}.{self.event}"

# pylint: disable=too-many-instance-attributes


@dataclass
class Control(TitleFromParents, NamedNode):
    " Form control "
    controlid: str
    datafield: str
    inputrequired: bool
    convertemptytonull: bool
    label: str
    formfor: str
    type: str
    eventlisteners: List[EventListener]

    def __post_init__(self):
        self.title = self.controlid

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
class Grid(TitleFromParents, NamedNode):
    " Table view control"
    columns: List[Control]

    def children(self):
        return self.columns


@dataclass
class SubForm(TitleFromParents, Commander, NamedNode):  # pylint: disable=too-many-instance-attributes
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

    def all_subforms(self) -> List[SubForm]:
        " returns all nested subforms"
        return list(filter(lambda x: isinstance(x, SubForm), self.all_objects()))


# pylint:disable=too-many-ancestors
@dataclass
class Report(Commander, PageOwner):
    " Report metadata "
    output_type: str
    formulas: List[str]
