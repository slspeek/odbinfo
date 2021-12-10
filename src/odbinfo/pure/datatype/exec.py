""" Executable datatypes and its containers """
from dataclasses import dataclass, field
from itertools import chain
from typing import List, Optional

from odbinfo.pure.datatype.base import BasicToken, WebPage, WebPageWithUses


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
class BasicCall:
    """ a function or procedure call in parsed basic code"""
    name_token: BasicToken
    module_token: Optional[BasicToken]


# pylint:disable=too-many-instance-attributes
@dataclass
class BasicFunction(WebPageWithUses):
    """ Basic sub or function """
    library: str
    module: str
    name_token_index: int = field(init=False)
    tokens: List[BasicToken] = field(init=False, default_factory=list)
    body_tokens: List[BasicToken] = field(
        init=False, repr=False, default_factory=list)
    calls: List[BasicCall] = field(init=False, default_factory=list)
    strings: List[BasicToken] = field(
        init=False, repr=False, default_factory=list)
    title: str = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.name}.{self.module}.{self.library}"

    def children(self):
        return self.tokens

    @property
    def script_url(self):
        """As matched in EventListener"""
        return \
            f"{self.library}.{self.module}.{self.name}"

    def to_dict(self):
        result = super().to_dict()
        del result["body_tokens"]
        del result["strings"]
        del result["calls"]
        return result


@dataclass
class Module(WebPage):
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

    def children(self):
        return chain(self.callables, self.tokens)

    def to_dict(self):
        callable_links = [func.identifier.__dict__ for func in self.callables]
        rdict = super().to_dict()
        rdict["callables"] = callable_links
        return rdict


@dataclass
class Library(WebPage):
    """ Basic library"""
    modules: List[Module]

    def children(self):
        return self.modules

    def to_dict(self):
        module_links = [module.identifier.__dict__ for module in self.modules]
        rdict = super().to_dict()
        rdict["modules"] = module_links
        return rdict

    @property
    def basicfunctions(self) -> List[BasicFunction]:
        """returns all basicfunctions in this library"""
        return sum((module.callables for module in self.modules), [])
