" Graphical User Interface datatypes "
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Union

from odbinfo.pure.datatype.base import NamedNode, User, WebPageWithUses
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
class DatabaseDisplay(User, NamedNode):
    " Field in TextDocument "
    database: str
    table: str
    tabletype: str
    index: int = field(init=False)


@dataclass
class TextDocument(WebPageWithUses):
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
class EventListener(User, NamedNode):
    " Control eventlistener "
    # event: str
    script: str

    def parsescript(self) -> str:
        "returns {Lib}.{Mod}.{Func} part from script field"
        return (self.script.split(":")[1]).split("?")[0]


@dataclass
# pylint: disable=too-many-instance-attributes
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
class Grid(NamedNode):
    " Table view control"
    columns: List[Control]
    type: str

    def children(self):
        return self.columns


@dataclass
# pylint: disable=too-many-instance-attributes
class SubForm(Commander, NamedNode):
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
class Form(WebPageWithUses):
    " Toplevel form "
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)

    def children(self):
        return self.subforms


# pylint:disable=too-many-ancestors
@dataclass
class Report(Commander, WebPageWithUses):
    " Report metadata "
    output_type: str
    formulas: List[str]

    def children(self):
        if self.embedded_query:
            return [self.embedded_query]
        return ()
