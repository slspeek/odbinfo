" super classes of the datatypes and reference types "
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, cast


@dataclass
class Identifier:
    " Unique id for ooobjects "
    object_type: str
    local_id: str
    bookmark: Optional[str] = field(init=False, default=None)


@dataclass
class Token:
    "lexer token"
    column: int
    line: int
    text: str
    type: int
    index: int
    hidden: bool
    link: Optional[Identifier] = field(init=False, default=None)


@dataclass
class LinkedString:
    " a string referencing a dataobject "
    text: str
    link: Optional[Identifier] = field(init=False, default=None)


@dataclass
class DataObject:
    " A node in the graph representation "\
        " Super class of the data objects that have a node of their own "
    name: str
    title: str = field(init=False)
    uses: List['DataObject'] = field(
        init=False, repr=False, default_factory=list)
    used_by: List['DataObject'] = field(
        init=False, repr=False, default_factory=list)
    # parent: Optional['DataObject'] = field(
    #     init=False, repr=False, default=None)
    parent_link: Optional['Identifier'] = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.title = self.name

    def children(self) -> Sequence['DataObject']:  # pylint:disable=no-self-use
        " returns a list of child nodes "
        return []

    def all_objects(self) -> Sequence['DataObject']:
        " returns all dataobjects for the graph "
        return_value: List['DataObject'] = [self]
        for child in self.children():
            return_value += cast(List['DataObject'], child.all_objects())

        return return_value

    def set_parents(self, parent: Optional['DataObject']) -> None:
        " recursively set parents "
        if parent:
            self.parent_link = get_identifier(parent)
        for child in self.children():
            child.set_parents(self)


def get_identifier(dataobject) -> Identifier:
    "returns Identifier for `dataobject`"
    classname = dataobject.__class__.__name__.lower()
    plurals = {"query": "queries",
               "pythonlibrary": "pythonlibraries",
               "library": "libraries"}
    plural = plurals.get(classname, classname + "s")
    return Identifier(plural,
                      dataobject.title)


@dataclass
class UseCase:
    " `obj` uses `subject`"
    obj: DataObject
    # ref_location: Union[None, Token, LinkedString]
    subject: DataObject
    type: str
