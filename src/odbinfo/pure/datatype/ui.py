""" Graphical User Interface datatypes """
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Union, cast

from odbinfo.pure.datatype import Usable
from odbinfo.pure.datatype.base import (Dependent, NamedNode, User,
                                        WebPageWithUses)
from odbinfo.pure.datatype.exec import BasicFunction
from odbinfo.pure.datatype.tabular import EmbeddedQuery

COMMAND_TYPE_COMMAND = ["command", "sql", "sql-pass-through"]


@dataclass  # type: ignore
class AbstractCommander(User, NamedNode, Dependent, ABC):
    """Commander interface"""

    # Only if commandtype in ["command", "sql", "sqlpassthrough"]
    embedded_query: Optional[EmbeddedQuery] = field(init=False, default=None)

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

    def consider_uses(self, target: Usable):
        if not self.issqlcommand and \
                target.users_match(self.command):
            self.link_to(target)


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

    def consider_uses(self, target: Usable):
        if target.users_match(self.table):
            self.link_to(target)


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

    def consider_uses(self, target: Usable):
        if not isinstance(target, BasicFunction):
            return
        func = cast(BasicFunction, target)
        if func.script_url == self.parsescript():
            self.link_to(func)


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

    def is_visible(self, config) -> bool:
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
class Control(ControlBase):
    """ Form control """

    @property
    def graph_label(self):
        if self.label:
            return self.label
        return super().graph_label


@dataclass
class ListBox(AbstractCommander, ControlBase):
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


@dataclass
class Grid(NamedNode):
    """ Table view control"""
    columns: List[Control]
    type: str

    def children(self):
        return self.columns


@dataclass
# pylint: disable=too-many-instance-attributes
class SubForm(Commander, NamedNode):
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


@dataclass
class Form(WebPageWithUses):
    """ Toplevel form """
    subforms: List[SubForm]
    height: Optional[int] = field(init=False, default=None)

    def children(self):
        return self.subforms


@dataclass
class Report(Commander, WebPageWithUses):
    """ Report metadata """
    output_type: str
    formulas: List[str]

    def children(self):
        if self.embedded_query:
            return [self.embedded_query]
        return ()
