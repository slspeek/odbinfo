""" Graphical User Interface datatypes """
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Union

from odbinfo.pure.datatype.base import (Dependent, NamedNode, Preprocessable,
                                        User, WebPageWithUses)
from odbinfo.pure.datatype.config import GraphConfig
from odbinfo.pure.datatype.tabular import EmbeddedQuery
from odbinfo.pure.visitor import PreprocessableVisitor

COMMAND_TYPE_COMMAND = ["command", "sql", "sql-pass-through"]


@dataclass  # type: ignore
class AbstractCommander(User, NamedNode, Dependent, ABC):
    """Commander interface"""

    # Only if commandtype in ["command", "sql", "sqlpassthrough"]
    embedded_query: Optional[EmbeddedQuery] = field(init=False, default=None)

    def __post_init__(self):
        if self.issqlcommand:
            self.embedded_query = \
                EmbeddedQuery(f"{self.name}.Command", self.command)

    @property
    @abstractmethod
    def command(self):
        """returns the command str"""

    @property
    @abstractmethod
    def commandtype(self):
        """returns the commandtype"""

    @property
    def issqlcommand(self):
        """returns True if command contains SQL"""
        return self.commandtype in COMMAND_TYPE_COMMAND

    def accept(self, visitor):
        visitor.visit_abstractcommander(self)


@dataclass
class Commander(AbstractCommander):
    """ Has a command and commandtype """
    cmd: str
    cmdtype: str

    @property
    def command(self):
        return self.cmd

    @property
    def commandtype(self):
        return self.cmdtype


@dataclass
class DatabaseDisplay(User, NamedNode, Dependent):
    """ Field in TextDocument """

    database: str
    table: str
    tabletype: str

    def accept(self, visitor):
        visitor.visit_databasedisplay(self)


@dataclass
class TextDocument(WebPageWithUses):
    """ ODT or OTT file metadata """
    filename: str
    path: str
    fields: List[DatabaseDisplay]

    def children(self):
        return self.fields

    def users_match(self, username: str) -> bool:
        # could be done better by enumerating all subpaths
        return username in (self.name, self.filename)


@dataclass
class EventListener(User, NamedNode, Dependent):
    """ Control eventlistener """

    script: str

    def parsescript(self) -> str:
        """returns {Lib}.{Mod}.{Func} part from script field"""
        return (self.script.split(":")[1]).split("?")[0]

    def accept(self, visitor):
        visitor.visit_eventlistener(self)


@dataclass
# pylint: disable=too-many-instance-attributes
class ControlBase(NamedNode):
    """ Form control """
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

    def is_visible(self, config: GraphConfig) -> bool:
        if not super().is_visible(config):
            return False
        if config.relevant_controls:
            return self.is_relevant()
        return True

    def is_relevant(self):
        """Returns True if this Control is interesting for the depencency graph"""
        if self.eventlisteners:
            return True
        return False


@dataclass
class Control(ControlBase, Preprocessable):
    """ Form control """

    @property
    def graph_label(self):
        if self.label:
            return self.label
        return super().graph_label

    def accept(self, visitor: PreprocessableVisitor):
        visitor.visit_control(self)


@dataclass
class ListBox(AbstractCommander, ControlBase, Preprocessable):
    """ ListBox control"""
    boundcolumn: int
    dropdown: bool
    listsourcetype: str
    listsource: str

    @property
    def command(self):
        return self.listsource

    @property
    def commandtype(self):
        return self.listsourcetype

    def is_relevant(self):
        if super().is_relevant():
            return True
        if self.embedded_query or self.link:
            return True
        return False

    def children(self):
        if self.embedded_query:
            return self.eventlisteners + [self.embedded_query]
        return self.eventlisteners

    def accept(self, visitor: PreprocessableVisitor):
        visitor.visit_listbox(self)


@dataclass
class Grid(NamedNode):
    """ Table view control"""
    columns: List[Control]
    type: str

    def children(self):
        return self.columns


@dataclass
# pylint: disable=too-many-instance-attributes
class SubForm(Commander, NamedNode, Preprocessable):
    """ Database subform """
    allowdeletes: str
    allowinserts: str
    allowupdates: str
    masterfields: str
    detailfields: str
    controls: List[Union[Control, Grid, ListBox]]
    subforms: List['SubForm']
    depth: Optional[int] = field(init=False, default=None)

    def children(self):
        return_value = self.controls + self.subforms
        if self.embedded_query:
            return_value += [self.embedded_query]
        return return_value

    def accept(self, visitor):
        visitor.visit_subform(self)


@dataclass
class Form(WebPageWithUses, Preprocessable):
    """ Toplevel form """
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)

    def children(self):
        return self.subforms

    def accept(self, visitor: PreprocessableVisitor):
        visitor.visit_form(self)


@dataclass
class Report(Commander, WebPageWithUses):
    """ Report metadata """

    def accept(self, visitor):
        visitor.visit_commander(self)

    output_type: str
    formulas: List[str]

    def __post_init__(self):
        Commander.__post_init__(self)
        WebPageWithUses.__post_init__(self)

    def children(self):
        if self.embedded_query:
            return [self.embedded_query]
        return ()
