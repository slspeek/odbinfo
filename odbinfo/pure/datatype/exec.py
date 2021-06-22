" Executable datatypes and its containers "
from dataclasses import dataclass, field
from typing import List, Sequence

from odbinfo.pure.datatype.base import DataObject, Token


@dataclass
class PythonModule(DataObject):
    " Python Module "
    library: str
    source: str

    def __post_init__(self):
        self.title = f"{self.library}.{self.name}"


@dataclass
class PythonLibrary(DataObject):
    " Python library "
    modules: List[PythonModule]

    def children(self) -> Sequence[DataObject]:
        return self.modules


@dataclass
class BasicCall:
    " a function or procedure call in parsed basic code"
    name_token: Token
    module_token: Token


# pylint:disable=too-many-instance-attributes
@dataclass
class BasicFunction(DataObject):
    " Basic sub or function "
    library: str
    module: str
    name_token_index: int = field(init=False)
    tokens: Sequence[Token] = field(init=False, default_factory=list)
    body_tokens: Sequence[Token] = field(
        init=False, repr=False, default_factory=list)
    calls: List[BasicCall] = field(init=False, default_factory=list)
    strings: List[Token] = field(init=False, repr=False,  default_factory=list)
    title: str = field(init=False)

    def __post_init__(self):
        # self.source = tohtml(self.source)
        self.title = f"{self.name}.{self.module}.{self.library}"


@dataclass
class Module(DataObject):
    " Basic module"
    library: str
    source: str
    callables: List[BasicFunction] = field(init=False, default_factory=list)
    title: str = field(init=False)
    tokens: List[Token] = field(init=False, default_factory=list)
    name_indexes: List[int] = field(init=False, default_factory=list)

    def __post_init__(self):
        # self.source = tohtml(self.source)
        self.title = f"{self.name}.{self.library}"

    def children(self) -> Sequence[DataObject]:
        return self.callables


@dataclass
class Library(DataObject):
    " Basic library"
    modules: List[Module]

    def children(self) -> Sequence[DataObject]:
        return self.modules
