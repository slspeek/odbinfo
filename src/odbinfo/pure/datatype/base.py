""" super classes of the datatypes and reference types """
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from itertools import chain
from typing import Any, List, Optional, cast

logger = logging.getLogger(__name__)


# pylint:disable=too-few-public-methods
class Dictable(ABC):
    """Dictionary representable"""

    @abstractmethod
    def to_dict(self):
        """ returns dictionary representation
            used for the write-out to the hugo site"""


@dataclass(frozen=True)
class Identifier(Dictable):
    """ Unique id for ooobjects """
    content_type: str
    local_id: str
    bookmark: Optional[str]

    def to_dict(self):
        adict = dict(self.__dict__)
        if not self.bookmark:
            del adict["bookmark"]
        return adict


def content_type(clazz) -> str:
    """returns the Hugo content type of `clazz`"""
    return clazz.__name__.lower()


def list_to_dict(values):
    """ convert list values to dict """
    if values:
        if isinstance(values[0], Dictable):
            return [d.to_dict() for d in values]
    return values


def to_dict(value: Any):
    """ returns dictionay representation of `value`"""
    if isinstance(value, List):
        return list_to_dict(value)
    if isinstance(value, Dictable):
        return value.to_dict()
    return value


@dataclass
class Node(Dictable):
    """ superclass of OO-objects representations """
    obj_id: str = field(init=False, default="OBJID_NOT_SET")
    parent: Optional["NamedNode"] = field(init=False, default=None, repr=False)

    @property
    def content_type(self) -> str:
        """ returns classname in lowercase """
        return content_type(self.__class__)

    @property
    def identifier(self):
        """returns a link to this node"""
        return get_identifier(self)

    # pylint:disable=no-self-use
    def children(self):
        """ returns a list of child nodes """
        return ()

    def all_objects(self):
        """ returns all nodes in the subtree with self as root """
        return_value = [self]
        for child in self.children():
            return_value = chain(return_value, child.all_objects())

        return return_value

    def to_dict(self):
        sdict = dict(self.__dict__)
        if "parent" in sdict:
            del sdict["parent"]
        for key, value in sdict.items():
            sdict[key] = to_dict(value)
        return sdict


@dataclass
class NamedNode(Node):
    """Has a name"""
    name: str


@dataclass
class User(Node):
    """ Mixin for Nodes that can use one other node"""
    link: Optional[Identifier] = field(init=False, default=None)

    def link_to(self, target: "Usable"):
        """links this object to `target`"""
        if self.link:
            logger.warning(
                "Replacing link in user: %s:%s (link was %s) with %s",
                self.content_type,
                self.obj_id,
                self.link,
                target.identifier
            )
        self.link = target.identifier


@dataclass
class Usable(NamedNode):
    """ Mixin for Nodes that can be used by other nodes """
    used_by: List['Identifier'] = field(
        init=False, repr=False, default_factory=list)

    def users_match(self, username: str) -> bool:
        """ determines whether `username` matches this object """
        return self.name == username


@dataclass
class UseAggregator(Node):
    """ aggregates uses and used_by """
    uses: List['Identifier'] = field(
        init=False, repr=False, default_factory=list)


@dataclass
class WebPage(NamedNode):
    """ has its own page, thus title attribute "\
        " an object with a parent_link """
    parent_link: Optional['Identifier'] = field(init=False, default=None)
    title: str = field(init=False, default="TITLE_NOT_SET")

    def __post_init__(self):
        self.title = self.name

    def set_parent_links(self, parent: Optional['WebPage']) -> None:
        """ recursively set parents """
        if isinstance(parent, WebPage):
            self.parent_link = parent.identifier

        for child in self.children():
            if isinstance(child, WebPage):
                child.set_parent_links(self)


@dataclass
class WebPageWithUses(Usable, UseAggregator, WebPage):
    """ WebPage with uses and used_by """


class NoWebPageAncestorException(Exception):
    """Inconsistent metadata exception"""

    def __init__(self, node: Node):
        self.node = node
        super().__init__(f"No WebPage ancestor for {node}")


def get_identifier(usable) -> Identifier:
    """returns Identifier for `usable`"""
    parent: Node = usable
    while not isinstance(parent, WebPage):
        if parent.parent is None:
            raise NoWebPageAncestorException(usable)
        parent = parent.parent
    webpage: WebPage = cast(WebPage, parent)
    if webpage is usable:
        return Identifier(usable.content_type,
                          usable.title, None)
    return Identifier(webpage.content_type,
                      webpage.title, usable.obj_id)


@dataclass
class TokenBase(User, Node):
    """lexer token"""
    text: str
    type: int
    index: int
    hidden: bool
    cls: Optional[str] = field(init=False, default=None)

    def to_dict(self):
        adict = super().to_dict()
        del adict["hidden"]
        if not self.link:
            del adict["obj_id"]
            if "link" in adict:
                del adict["link"]
        return adict


@dataclass
class SQLToken(TokenBase):
    """SQL lexer token"""

    def to_dict(self):
        adict = super().to_dict()
        del adict["index"]
        return adict


@dataclass
class Token(TokenBase):
    """Token for BasicFunctions"""


class Dependent(ABC):
    """Depends on zero of more Usable instances"""

    @abstractmethod
    def link_uses(self, target: Usable):
        """Match `target` among its Users"""