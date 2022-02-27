"""Node visitor interfaces"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from odbinfo.pure.datatype.base import BasicToken
from odbinfo.pure.datatype.basicfunction import BasicFunction

if TYPE_CHECKING:
    from odbinfo.pure.datatype.exec import Module
    from odbinfo.pure.datatype.tabular import Key, QueryBase
    from odbinfo.pure.datatype.ui import (AbstractCommander, Control,
                                          DatabaseDisplay, EventListener, Form,
                                          ListBox, SubForm)


class BasicTokenVisitor(ABC):
    """ BasicToken visitor interface"""

    @abstractmethod
    def visit_basictoken(self, token: BasicToken):
        """ visit a BASIC token"""


class ListBoxVisitor(ABC):
    """ ListBox visitor interface """

    @abstractmethod
    def visit_listbox(self, listbox: ListBox):
        """visit listbox"""


class SubFormVisitor(ABC):
    """ SubForm visitor interface"""

    @abstractmethod
    def visit_subform(self, subform: SubForm):
        """Visit SubForm"""


class ControlVisitor(ABC):
    """ Control visitor interface"""

    @abstractmethod
    def visit_control(self, control: Control):
        """Visit Control"""


class FormVisitor(SubFormVisitor, ListBoxVisitor, ControlVisitor, ABC):
    """ Form visitor interface """

    @abstractmethod
    def visit_form(self, form: Form):
        """Visit Form"""


class ModuleVisitor(ABC):
    """ Module visitor interface """

    @abstractmethod
    def visit_module(self, module: Module):
        """Visit Module"""


class QueryBaseVisitor(ABC):
    """QueryBase visitor interface"""

    @abstractmethod
    def visit_querybase(self, query: QueryBase):
        """Visit QueryBase"""


class PreprocessableVisitor(ModuleVisitor, QueryBaseVisitor, FormVisitor, ABC):
    """ Preprocessable visitor interface """


class KeyVisitor(ABC):
    """Visitor interface for Key"""

    @abstractmethod
    def visit_key(self, key: Key):
        """visit key"""


class EventListenerVisitor(ABC):
    """Visitor interface for EventListener"""

    @abstractmethod
    def visit_eventlistener(self, eventlistener: EventListener):
        """visit the eventlistener"""


class CommanderVisitor(SubFormVisitor, ListBoxVisitor, ABC):
    """Commander visitor interface"""

    @abstractmethod
    def visit_commander(self, commander: AbstractCommander):
        """visit the commander"""


class DatabaseDisplayVisitor(ABC):
    """DatabaseDisplay visitor interface """

    @abstractmethod
    def visit_databasedisplay(self, display: DatabaseDisplay):
        """visit a database display"""


class BasicFunctionVisitor(ABC):
    """BasicFucntion visitor interface """

    @abstractmethod
    def visit_basicfunction(self, basicfunction: BasicFunction):
        """ visit a basicfunction """


class DependentVisitor(KeyVisitor, QueryBaseVisitor, EventListenerVisitor,
                       CommanderVisitor, DatabaseDisplayVisitor,
                       BasicFunctionVisitor, ABC):
    """ Dependent visitor interface"""
