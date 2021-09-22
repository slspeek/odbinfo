" super classes of the datatypes and reference types "
from dataclasses import dataclass, field
from itertools import chain
from typing import List, Optional, cast


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
    " superclass of OO-objects representations "
    obj_id: str = field(init=False, default="OBJID_NOT_SET")
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


@dataclass
class UseAggregator:
    " aggregates uses and used_by "
    uses: List['Identifier'] = field(
        init=False, repr=False, default_factory=list)


@dataclass
class WebPage(NamedNode):
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


@dataclass
class WebPageWithUses(Usable, UseAggregator, WebPage):
    " WebPage with uses and used_by "


def get_identifier(usable: Node) -> Identifier:
    "returns Identifier for `usable`"
    parent: Node = usable
    while not isinstance(parent, WebPage):
        if parent.parent is None:
            raise RuntimeError("No WebPage ancestor for %s" % usable)
        parent = parent.parent
    parent = cast(WebPage, parent)
    if parent == usable:
        return Identifier(parent.content_type(),
                          parent.title, None)
    return Identifier(parent.content_type(),
                      parent.title, usable.obj_id)


@dataclass
class Token(User, Node):
    "lexer token"
    text: str
    type: int
    index: int
    hidden: bool
    cls: Optional[str] = field(init=False, default=None)
