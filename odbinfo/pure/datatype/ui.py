" Graphical User Interface datatypes "
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Union

from odbinfo.pure.datatype.base import (NamedNode, Node, PageOwner,
                                        TitleFromParents, User)
from odbinfo.pure.datatype.tabular import EmbeddedQuery


@dataclass  # type: ignore
class AbstractCommander(User, ABC):
    "Commander interface"

    # Only if commandtype in ["command", "sql", "sqlpassthrough"]
    embedded_query: Optional[EmbeddedQuery] = field(init=False, default=None)

    @abstractmethod
    def get_command(self):
        "returns the command str"

    @abstractmethod
    def get_commandtype(self):
        "returns the commandtype"


@dataclass
class Commander(AbstractCommander):
    " Has a command and commandtype "
    command: str
    commandtype: str

    def get_command(self):
        return self.command

    def get_commandtype(self):
        return self.commandtype


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
class EventListener(User, Node):
    " Control eventlistener "
    event: str
    script: str

    def set_title(self):
        " sets a unique title "
        self.title = f"{self.parent.title}.{self.event}"

    def parsescript(self) -> str:
        "returns {Lib}.{Mod}.{Func} part from script field"
        return (self.script.split(":")[1]).split("?")[0]
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
class ListBox(AbstractCommander, Control):
    " ListBox control"
    boundcolumn: int
    dropdown: bool
    listsourcetype: str
    listsource: str

    def get_command(self):
        return self.listsource

    def get_commandtype(self):
        return self.listsourcetype

    def children(self):

        if self.embedded_query:
            return self.eventlisteners + [self.embedded_query]
        return self.eventlisteners


@dataclass
class Grid(TitleFromParents, NamedNode):
    " Table view control"
    columns: List[Control]
    type: str

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
        return_value = self.controls + self.subforms
        if self.embedded_query:
            return_value += [self.embedded_query]
        return return_value


@dataclass
class Form(PageOwner):
    " Toplevel form "
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)

    def children(self):
        return self.subforms

    # def all_subforms(self) -> List[SubForm]:
    #     " returns all nested subforms"
    #     return list(filter(lambda x: isinstance(x, SubForm), self.all_objects()))


# pylint:disable=too-many-ancestors
@dataclass
class Report(Commander, PageOwner):
    " Report metadata "
    output_type: str
    formulas: List[str]

    def children(self):
        if self.embedded_query:
            return [self.embedded_query]
        return ()
