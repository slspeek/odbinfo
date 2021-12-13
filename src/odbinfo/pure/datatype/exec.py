""" Executable datatypes and its containers """
from dataclasses import dataclass, field
from itertools import chain
from typing import List, Optional

from odbinfo.pure.datatype import Usable
from odbinfo.pure.datatype.base import (Dependent, Token, WebPage,
                                        WebPageWithUses)


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


def equals_ignore_case(left: str, right: str) -> bool:
    """Compares `left` to `right` ignoring case"""
    return left.upper() == right.upper()


@dataclass
class BasicToken(Token):
    """BasicToken for BasicFunctions"""

    def match(self, target: str):
        """Matches `target` ignoring case to the text attribute"""
        return equals_ignore_case(self.text, target)


@dataclass
class BasicCall:
    """ a function or procedure call in parsed basic code"""
    name_token: BasicToken
    module_token: Optional[BasicToken]

    def match_module(self, target: "BasicFunction") -> bool:
        """Match module names"""
        if self.module_token:
            return self.module_token.match(target.module)
        # If module_token is not set we have a match
        return True

    def consider_use(self, target: "BasicFunction"):
        """Consider `target` for this call"""
        if not self.match_module(target):
            return
        if self.name_token.match(target.name) \
                and not self.name_token.link:
            self.name_token.link_to(target)


# pylint:disable=too-many-instance-attributes
@dataclass
class BasicFunction(WebPageWithUses, Dependent):
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

    def consider_calls(self, target: "BasicFunction"):
        """ find calls in `source` to `candidate_callee`"""
        for function_call in self.calls:
            function_call.consider_use(target)

    def consider_uses(self, target: Usable):
        if isinstance(target, BasicFunction):
            raise ValueError("Call consider_calls with a BasicFunction")
        self.consider_string_references(target)

    def consider_string_references(self, target: Usable):
        """Consider string references to `target`"""
        for string_literal in self.strings:
            if target.users_match(string_literal.text[1:-1]):
                string_literal.link_to(target)

    def remove_recursive_calls(self):
        """ Removes recursive calls
            to avoid linking every function to itself
            because of the way a return value is specified"""
        for call in self.calls:
            if call.module_token:
                continue
            if call.name_token.match(self.name):
                call.name_token.link = None

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
