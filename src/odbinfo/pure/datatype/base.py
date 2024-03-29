""" super classes of the datatypes and reference types """
from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from itertools import chain
from typing import List, Optional, cast

from odbinfo.pure.datatype.config import GraphConfig
from odbinfo.pure.datatype.dictable import Dictable, to_dict

logger = logging.getLogger(__name__)


def hugo_filename(name: str) -> str:
    """ name converted as hugo converts filename to .Params.filename
        See: https://gohugo.io/functions/anchorize/ """
    return name.replace(" ", "-").lower()


@dataclass(frozen=True)
class Identifier(Dictable):
    """ Unique id for (database) components """
    content_type: str
    local_id: str
    bookmark: Optional[str]

    @property
    def href(self):
        """Returns href for the graph.
        This is used to place a link in the diagram back to the hugo site,
        for each node in the diagram.
        """
        # NB: relies on all graphs to be in 'svg/' subfolder
        url = f"../{self.content_type}/{hugo_filename(self.local_id)}/index.html"
        if self.bookmark:
            url = f"{url}#{self.bookmark}"
        return url

    def to_dict(self):
        adict = dict(self.__dict__)
        if not self.bookmark:
            del adict["bookmark"]
        return adict


@dataclass(frozen=True)
class UseLink(Dictable):
    """ A link with source ids """
    link: Identifier
    sources: List[str]

    def to_dict(self):
        result = {
            "link": self.link.to_dict(),
            "sources": ",".join(self.sources)
        }
        if len(self.sources) > 1:
            result["mul"] = len(self.sources)
        return result


def content_type(clazz) -> str:
    """Returns the Hugo content type name for `clazz`"""
    return clazz.__name__.lower()


class TreeNode:
    """Base class for tree nodes"""

    # pylint:disable=no-self-use
    def children(self):
        """ Returns a list of child nodes """
        return ()

    def all_objects(self):
        """ Returns all nodes in the subtree with self as root """
        return_value = [self]
        for child in self.children():
            return_value = chain(return_value, child.all_objects())

        return return_value


@dataclass
class Node(Dictable, TreeNode):
    """ Superclass of OO-component metadata classes """
    obj_id: str = field(init=False, default="OBJID_NOT_SET")
    parent: Optional["NamedNode"] = field(init=False, default=None, repr=False)

    @property
    def content_type(self) -> str:
        """ Returns classname in lowercase """
        return content_type(self.__class__)

    @property
    def identifier(self):
        """Returns a link to this node"""
        return get_identifier(self)

    @property
    def href(self):
        """Returns href for the graph"""
        return self.identifier.href

    def to_dict(self):
        sdict = dict(self.__dict__)
        if "parent" in sdict:
            del sdict["parent"]
        for key, value in sdict.items():
            sdict[key] = to_dict(value)
        return sdict

    # TODO move out
    def is_visible(self, config: GraphConfig) -> bool:
        """Is the node visible in the graph"""
        if self.content_type in config.excludes:
            return False
        return True


@dataclass
class NamedNode(Node):
    """Has a name"""
    name: str

    @property
    def graph_label(self):
        """Label for the node in the graph"""
        return self.name


@dataclass
class User(Node):
    """ Mixin for Nodes that can use at most one other node"""
    link: Optional[Identifier] = field(init=False, default=None)

    def link_to(self, target: "Usable"):
        """links this object to `target`"""
        if self.link:
            logger.warning(
                "Replacing link in user: %s:%s (link was %s) with %s",
                self.content_type, self.obj_id, self.link, target.identifier)
        self.link = target.identifier


@dataclass
class Usable(NamedNode):
    """ Mixin for Nodes that can be used by other nodes """
    used_by: List['Identifier'] = field(init=False,
                                        repr=False,
                                        default_factory=list)

    def is_reference_match(self, referring: str) -> bool:
        """ Determines whether `referring` string matches this object """
        return self.name == referring


@dataclass
class UseAggregator(Node, ABC):
    """ Mixin for aggregating uses from children.
     E.g. a query object does not not directly refer to a table,
     but one of its SQLTokens does.
     Likewise for a Form containing a Control with an EventListener that uses BasicFunction.
    """
    uses: List['UseLink'] = field(init=False, repr=False, default_factory=list)


@dataclass
class WebPage(NamedNode, ABC):
    """ Has its own page,
        thus title attribute, which must be unique within the content_type.
        Can have a parent_link
        See metadata.TopLevelDisplayedContent.
    """
    parent_link: Optional['Identifier'] = field(init=False, default=None)
    title: str = field(init=False, default="TITLE_NOT_SET")

    def __post_init__(self):
        self.title = self.name

    def set_parent_links(self, parent: Optional['WebPage']) -> None:
        """ Recursively set parent links """
        if isinstance(parent, WebPage):
            self.parent_link = parent.identifier

        for child in self.children():
            if isinstance(child, WebPage):
                child.set_parent_links(self)


@dataclass
class WebPageWithUses(Usable, UseAggregator, WebPage, ABC):
    """ WebPage with uses and used_by """


class NoWebPageAncestorException(Exception):
    """Inconsistent metadata exception"""

    def __init__(self, node: Node):
        self.node = node
        super().__init__(f"No WebPage ancestor for {node}")


def get_identifier(node) -> Identifier:
    """returns Identifier for `node`"""
    parent: Node = node
    while not isinstance(parent, WebPage):
        if parent.parent is None:
            raise NoWebPageAncestorException(node)
        parent = parent.parent
    webpage: WebPage = cast(WebPage, parent)
    if webpage is node:
        return Identifier(node.content_type, node.title, None)
    return Identifier(webpage.content_type, webpage.title, node.obj_id)


@dataclass
class Token(User, Node):
    """lexer token"""
    text: str
    type: int
    index: int
    hidden: bool
    cls: Optional[str] = field(init=False, default=None)

    def to_dict(self):
        adict = super().to_dict()
        del adict["hidden"]
        del adict["type"]
        if not self.link:
            del adict["obj_id"]
            if "link" in adict:
                del adict["link"]
        return adict


def equals_ignore_case(left: str, right: str) -> bool:
    """Compares `left` to `right` ignoring case"""
    return left.upper() == right.upper()


@dataclass
class SQLToken(Token):
    """SQL lexer token"""

    def to_dict(self):
        adict = super().to_dict()
        del adict["index"]
        return adict


class Visitable(ABC):
    """Implementors can be visited"""

    @abstractmethod
    def accept(self, visitor):
        """Accept a `visitor`"""


@dataclass
class BasicToken(Token, Visitable):
    """BasicToken for BasicFunctions"""

    def match(self, target: str):
        """Matches `target` ignoring case to the text attribute"""
        return equals_ignore_case(self.text, target)

    def accept(self, visitor):
        visitor.visit_basictoken(self)


class Dependent(Visitable, ABC):
    """Is used as a source (referring component) in dependency search.
    """


class Preprocessable(Visitable, ABC):
    """Classes that need processing before dependency search"""
