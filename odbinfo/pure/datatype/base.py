" super classes of the datatypes and reference types "
from dataclasses import dataclass, field
from itertools import chain
from typing import List, Optional


@dataclass(frozen=True)
class Identifier:
    " Unique id for ooobjects "
    content_type: str
    local_id: str
    bookmark: Optional[str]


def content_type(clazz) -> str:
    "returns the Hugo content type of `clazz`"
    return clazz.__name__.lower()


@dataclass
class Node:
    " DataObject without children "
    obj_id: str = field(init=False, default="OBJID_NOT_SET")
    # title: str = field(init=False, default="TITLE_NOT_SET")
    parent: Optional["NamedNode"] = field(init=False, default=None, repr=False)

    def content_type(self) -> str:
        " returns classname in lowercase "
        return content_type(self.__class__)

    @property
    def identifier(self):
        "returns a link to this node"
        return get_identifier(self)

    # pylint:disable=no-self-use
    def children(self):
        " returns a list of child nodes "
        return ()

    def all_objects(self):
        " returns all nodes in the subtree with self as root "
        return_value = [self]
        for child in self.children():
            return_value = chain(return_value, child.all_objects())

        return return_value


@dataclass
class NamedNode(Node):
    "Has a name"
    name: str

    # def __post_init__(self):
    #     self.title = self.name
    #
    # def set_title(self):
    #     " sets a unique title "

    def users_match(self, username: str) -> bool:
        " determines whether `username` matches this object "
        return self.name == username


@dataclass
class User:
    " Mixin for Nodes that can use one other node"
    link: Optional[Identifier] = field(init=False, default=None)


@dataclass
class Usable:
    " Mixin for Nodes that can be used by other nodes "
    used_by: List['Identifier'] = field(
        init=False, repr=False, default_factory=list)

    # def users_match(self, username: str) -> bool:
    #     " determines whether `username` (possibly) matches this object "
    #     # pylint:disable=no-member
    #     return self.name == username  # type: ignore
    #     # return False


@dataclass
class UseAggregator:
    " aggregates uses and used_by "
    uses: List['Identifier'] = field(
        init=False, repr=False, default_factory=list)


@dataclass
class WebPage(UseAggregator, Usable, NamedNode):
    " has its own page, thus title attribute "\
        " an object with a parent_link "
    parent_link: Optional['Identifier'] = field(init=False, default=None)
    title: str = field(init=False, default="TITLE_NOT_SET")

    def __post_init__(self):
        self.title = self.name

    def set_parents(self, parent: Optional['WebPage']) -> None:
        " recursively set parents "
        if isinstance(parent, WebPage):
            self.parent_link = get_identifier(parent)

        for child in self.children():
            if isinstance(child, WebPage):
                child.set_parents(self)


def get_identifier(usable) -> Identifier:
    "returns Identifier for `usable`"
    parent = usable
    while not isinstance(parent, WebPage):
        parent = parent.parent
    if parent == usable:
        return Identifier(usable.content_type(),
                          usable.title, None)
    return Identifier(parent.content_type(),
                      parent.title, usable.obj_id)


# # pylint:disable=too-few-public-methods,no-member
# class TitleFromParents:
#     " set_title mixin "
#
#     def set_title(self):
#         " sets a unique title "
#         parent = self
#         while True:
#             # statement (s)
#             parent = parent.parent
#             self.title += f".{parent.name}"
#             if isinstance(parent, WebPage):
#                 break


@dataclass
class Token(User, Node):
    "lexer token"
    text: str
    type: int
    index: int
    hidden: bool

    # def __post_init__(self):
    #     self.title = f"token{self.index}"
    #
    # def set_title(self):
    #     " sets a unique title "
    #     self.title = f"{self.title}.{self.parent.title}"
