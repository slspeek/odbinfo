" super classes of the datatypes and reference types "
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Identifier:
    " Unique id for ooobjects "
    object_type: str
    local_id: str
    bookmark: Optional[str]


@dataclass(frozen=True)
class SourceIdentifier(Identifier):
    " source location identifier for back linking "
    location_id: str


@dataclass
class Node:
    " DataObject without children "
    obj_id: str = field(init=False, default="OBJID_NOT_SET")
    title: str = field(init=False, default="TITLE_NOT_SET")
    parent: Optional["NamedNode"] = field(init=False, default=None)

    def type_name(self):
        " returns classname in lowercase "
        return self.__class__.__name__.lower()

    # pylint:disable=no-self-use
    def children(self):
        " returns a list of child nodes "
        return []

    def all_objects(self):
        " returns all dataobjects for the graph "
        return_value = [self]
        for child in self.children():
            return_value += child.all_objects()

        return return_value


@dataclass
class NamedNode(Node):
    "Has a name"
    name: str

    def __post_init__(self):
        self.title = self.name

    def set_title(self):
        " sets a unique title "

    def users_match(self, username: str) -> bool:
        " determines whether `username` (possibly) matches this object "
        return self.name == username


@dataclass
class User:
    " Mixin for Nodes that can use other nodes "
    link: Optional[Identifier] = field(init=False, default=None)


@dataclass
class Usable:
    " Mixin for Nodes that can be used by other nodes "
    used_by: List['SourceIdentifier'] = field(
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
class PageOwner(UseAggregator, Usable, NamedNode):
    " has its own page, thus title attribute "\
        " an object with a parent_link "
    parent_link: Optional['Identifier'] = field(init=False, default=None)

    def set_parents(self, parent: Optional['PageOwner']) -> None:
        " recursively set parents "
        if isinstance(parent, PageOwner):
            self.parent_link = get_identifier(parent)

        for child in self.children():
            if isinstance(child, PageOwner):
                child.set_parents(self)


def get_identifier(usable) -> Identifier:
    "returns Identifier for `usable`"
    parent = usable
    while not isinstance(parent, PageOwner):
        parent = parent.parent
    if parent == usable:
        return Identifier(usable.type_name(),
                          usable.title, None)
    return Identifier(parent.type_name(),
                      parent.title, usable.obj_id)


def get_source_identifier(source: PageOwner, location: Optional[Node]) -> SourceIdentifier:
    " creates a SourceIdentifier "
    source_id = "" if not location else location.obj_id
    return SourceIdentifier(source.type_name(), source.title, None, source_id)


# pylint:disable=too-few-public-methods,no-member
class TitleFromParents:
    " set_title mixin "

    def set_title(self):
        " sets a unique title "
        parent = self
        while True:
            # statement (s)
            parent = parent.parent
            self.title += f".{parent.name}"
            if isinstance(parent, PageOwner):
                break


@dataclass
class Token(User, Node):
    "lexer token"
    text: str
    type: int
    index: int
    hidden: bool

    def __post_init__(self):
        self.title = f"token{self.index}"

    def set_title(self):
        " sets a unique title "
        self.title = f"{self.title}.{self.parent.title}"
