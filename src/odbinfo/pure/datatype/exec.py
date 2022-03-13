""" Executable datatypes and its containers """
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import chain
from typing import TYPE_CHECKING, List

from odbinfo.pure.datatype.base import BasicToken, Preprocessable, WebPage
from odbinfo.pure.datatype.basicfunction import BasicFunction

if TYPE_CHECKING:
    from odbinfo.pure.visitor import ModuleVisitor


@dataclass
class PythonModule(WebPage):
    """ Python Module metadata """
    library: str
    source: str

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.library}.{self.name}"


@dataclass
class PythonLibrary(WebPage):
    """ Python library metadata """
    modules: List[PythonModule]

    def children(self):
        return self.modules


@dataclass
class Module(WebPage, Preprocessable):
    """ Basic module metadata """

    library: str
    source: str
    callables: List[BasicFunction] = field(init=False, default_factory=list)
    title: str = field(init=False)
    tokens: List[BasicToken] = field(init=False, default_factory=list)
    name_indexes: List[int] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.name}.{self.library}"

    def children(self):
        return chain(self.callables, self.tokens)

    def to_dict(self):
        rdict = super().to_dict()
        rdict["callables"] = [
            func.identifier.to_dict() for func in self.callables
        ]
        return rdict

    def accept(self, visitor: ModuleVisitor):
        visitor.visit_module(self)


@dataclass
class Library(WebPage):
    """ Basic library metadata """
    modules: List[Module]

    def children(self):
        return self.modules

    def to_dict(self):
        rdict = super().to_dict()
        rdict["modules"] = [
            module.identifier.to_dict() for module in self.modules
        ]
        return rdict

    @property
    def basicfunctions(self) -> List[BasicFunction]:
        """ Returns all BasicFunctions in this library """
        return sum((module.callables for module in self.modules), [])
