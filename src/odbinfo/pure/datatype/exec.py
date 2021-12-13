""" Executable datatypes and its containers """
import dataclasses
from dataclasses import dataclass, field
from itertools import chain
from typing import List

from odbinfo.pure.datatype.base import BasicToken, Preprocessable, WebPage
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic


@dataclass
class PythonModule(WebPage):
    """ Python Module """
    library: str
    source: str

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.library}.{self.name}"


@dataclass
class PythonLibrary(WebPage):
    """ Python library """
    modules: List[PythonModule]

    def children(self):
        return self.modules


@dataclass
class Module(WebPage, Preprocessable):
    """ Basic module"""

    library: str
    source: str
    callables: List[BasicFunction] = field(init=False, default_factory=list)
    title: str = field(init=False)
    tokens: List[BasicToken] = field(init=False, default_factory=list)
    name_indexes: List[int] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.name}.{self.library}"

    def link_name_tokens(self):
        """Link the name tokens to the single function pages"""
        for name_index, acallable in zip(self.name_indexes, self.callables):
            self.tokens[name_index].link_to(acallable)

    def copy_tokens(self):
        """Copies the modules tokens"""
        self.tokens = [dataclasses.replace(token) for token in self.tokens]

    def preprocess(self):
        """ Tokenizes, parses, copies the tokens and sets the indexes
               of the tokens that are the names of the procedures """
        self.tokens = \
            get_basic_tokens(self.source)
        self.callables = \
            scan_basic(self.tokens, self.library, self.name)
        self.copy_tokens()
        self.name_indexes = \
            [c.name_token_index for c in self.callables]
        self.link_name_tokens()

    def children(self):
        return chain(self.callables, self.tokens)

    def to_dict(self):
        rdict = super().to_dict()
        rdict["callables"] = [
            func.identifier.to_dict() for func in self.callables]
        return rdict


@dataclass
class Library(WebPage):
    """ Basic library"""
    modules: List[Module]

    def children(self):
        return self.modules

    def to_dict(self):
        rdict = super().to_dict()
        rdict["modules"] = [module.identifier.to_dict()
                            for module in self.modules]
        return rdict

    @property
    def basicfunctions(self) -> List[BasicFunction]:
        """returns all basicfunctions in this library"""
        return sum((module.callables for module in self.modules), [])
