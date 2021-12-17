"""Node visitor interfaces"""

from abc import ABC, abstractmethod

from odbinfo.pure.datatype.exec import Module
from odbinfo.pure.datatype.tabular import QueryBase
from odbinfo.pure.datatype.ui import Control, Form, Grid, ListBox, SubForm


class ModuleVisitor(ABC):
    """ Module visitor interface """
    @abstractmethod
    def visit_module(self, module: Module):
        """Visit Module"""


class PreprocessableVisitor(ModuleVisitor, ABC):
    """ Preprocessable visitor interface """

    @abstractmethod
    def visit_querybase(self, query: QueryBase):
        """Visit QueryBase"""

    @abstractmethod
    def visit_form(self, form: Form):
        """Visit Form"""

    @abstractmethod
    def visit_subform(self, subform: SubForm):
        """Visit SubForm"""

    @abstractmethod
    def visit_control(self, control: Control):
        """Visit Control"""

    @abstractmethod
    def visit_grid(self, grid: Grid):
        """Visit Grid"""

    @abstractmethod
    def visit_listbox(self, listbox: ListBox):
        """Visit ListBox"""
