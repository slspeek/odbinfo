"""Node visitor interfaces"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from odbinfo.pure.datatype.exec import Module
    from odbinfo.pure.datatype.tabular import Key, QueryBase
    from odbinfo.pure.datatype.ui import (AbstractCommander, Control,
                                          EventListener, Form, Grid, ListBox,
                                          SubForm)


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


class FormVisitor(SubFormVisitor, ListBoxVisitor, ABC):
    """ Form visitor interface """

    @abstractmethod
    def visit_form(self, form: Form):
        """Visit Form"""

    @abstractmethod
    def visit_control(self, control: Control):
        """Visit Control"""

    @abstractmethod
    def visit_grid(self, grid: Grid):
        """Visit Grid"""


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


class KeyVisitor:
    """Visitor interface for Key"""

    @abstractmethod
    def visit_key(self, key: Key):
        """visit key"""


class EventListenerVisitor:
    """Visitor interface for EventListener"""

    @abstractmethod
    def visit_eventlistener(self, eventlistener: EventListener):
        """visit the eventlistener"""


class CommanderVisitor(SubFormVisitor, ListBoxVisitor):
    """Commander visitor interface"""

    @abstractmethod
    def visit_commander(self, commander: AbstractCommander):
        """visit the commander"""


class DependentVisitor(KeyVisitor,
                       QueryBaseVisitor,
                       EventListenerVisitor,
                       CommanderVisitor,
                       ABC):
    """ Dependent visitor interface"""
