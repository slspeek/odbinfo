"""basicfunction class"""
from dataclasses import dataclass, field
from typing import List, Optional

from odbinfo.pure.datatype.base import BasicToken, Dependent, WebPageWithUses


@dataclass
class BasicCall:
    """ A function or procedure call in parsed basic code"""
    name_token: BasicToken
    module_token: Optional[BasicToken]

    def match_module(self, module_name: str) -> bool:
        """Match module names"""
        if self.module_token:
            return self.module_token.match(module_name)
        # If module_token is not set we have a match
        return True

    def consider_use(self, target: "BasicFunction"):
        """Consider `target` for this call"""
        if self.name_token.link:
            # if already linked do nothing
            return
        if not self.match_module(target.module):
            return
        if self.name_token.match(target.name):
            self.name_token.link_to(target)


# pylint:disable=too-many-instance-attributes
@dataclass
class BasicFunction(WebPageWithUses, Dependent):
    """ Basic procedure or function metadata"""

    library: str
    module: str
    name_token_index: int = field(init=False)
    tokens: List[BasicToken] = field(init=False, default_factory=list)
    body_tokens: List[BasicToken] = field(init=False,
                                          repr=False,
                                          default_factory=list)
    calls: List[BasicCall] = field(init=False, default_factory=list)
    strings: List[BasicToken] = field(init=False,
                                      repr=False,
                                      default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.title = f"{self.name}.{self.module}.{self.library}"

    def accept(self, visitor):
        visitor.visit_basicfunction(self)

    def children(self):
        return self.tokens

    def to_dict(self):
        result = super().to_dict()
        del result["body_tokens"]
        del result["strings"]
        del result["calls"]
        return result
