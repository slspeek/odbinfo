" super classes of the datatypes and reference types "
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Identifier:
    " Unique id for ooobjects "
    object_type: str
    local_id: str
    bookmark: Optional[str] = field(init=False, default=None)


@dataclass
class SourceIdentifier(Identifier):
    " source location identifier for back linking "
    location_id: str


@dataclass
class Node:
    " DataObject without children "
    obj_id: str = field(init=False, default="not-set")

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
    parent: Optional["NamedNode"] = field(init=False, default=None)


@dataclass
class LinkedString:
    " a string referencing a dataobject "
    text: str
    link: Optional[Identifier] = field(init=False, default=None)


@dataclass
class Aggregator:
    " aggregates uses and used_by "
    uses: List['Identifier'] = field(
        init=False, repr=False, default_factory=list)
    used_by: List['SourceIdentifier'] = field(
        init=False, repr=False, default_factory=list)


@dataclass
class PageOwner(Aggregator, NamedNode):
    " has its own page, thus title attribute "\
        " an object with a parent_link "
    title: str = field(init=False)
    parent_link: Optional['Identifier'] = field(init=False, default=None)

    def __post_init__(self):
        self.title = self.name

    def set_parents(self, parent: Optional['PageOwner']) -> None:
        " recursively set parents "
        if isinstance(parent, PageOwner):
            self.parent_link = get_identifier(parent)

        for child in self.children():
            if isinstance(child, PageOwner):
                child.set_parents(self)


def get_identifier(page: PageOwner) -> Identifier:
    "returns Identifier for `dataobject`"
    return Identifier(page.type_name(),
                      page.title)


def get_source_identifier(source: PageOwner, location: Optional[Node]) -> SourceIdentifier:
    " creates a SourceIdentifier "
    source_id = "" if not location else location.obj_id
    return SourceIdentifier(source.type_name(), source.title, source_id)


@dataclass
class UseCase:
    " `obj` uses `subject`"
    obj: SourceIdentifier
    subject: Identifier
    type: str


def use_case(source: PageOwner,
             location: Optional[Node],
             target: PageOwner,
             ref_type: str) -> UseCase:
    " creates a usecase from `source` and `location` to `target`"
    return UseCase(get_source_identifier(source, location), get_identifier(target), ref_type)


@dataclass
class Token(Node):
    "lexer token"
    text: str
    type: int
    index: int
    hidden: bool
    link: Optional[Identifier] = field(init=False, default=None)
