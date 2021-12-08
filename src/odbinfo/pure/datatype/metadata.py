""" Metadata class """
import itertools
from dataclasses import dataclass, field
from enum import Enum
from itertools import chain
from typing import Iterable, List, Sequence, cast

from graphviz import Digraph

from odbinfo.pure.datatype.base import Node, Token, Usable, User, WebPage
from odbinfo.pure.datatype.exec import (BasicFunction, Library, Module,
                                        PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import EmbeddedQuery, Query, Table, View
from odbinfo.pure.datatype.ui import (AbstractCommander, EventListener, Form,
                                      Report, TextDocument)


class TopLevelDisplayedContent(Enum):
    """These contenttypes have a webpage of their own in the generated report"""
    TABLE = "table"
    QUERY = "query"
    VIEW = "view"
    FORM = "form"
    REPORT = "report"
    BASICFUNCTION = "basicfunction"
    MODULE = "module"
    LIBRARY = "library"
    PYTHONLIBRARY = "pythonlibrary"
    PYTHONMODULE = "pythonmodule"
    TEXTDOCUMENT = "textdocument"


# pylint: disable=too-many-instance-attributes
@dataclass
class Metadata(WebPage):
    """ Collector class for all metadata read from the odb-file """
    table_defs: List[Table]
    view_defs: List[View]
    query_defs: List[Query]
    form_defs: List[Form]
    report_defs: List[Report]
    library_defs: List[Library]
    pythonlibrary_defs: List[PythonLibrary]
    textdocument_defs: List[TextDocument]
    graphs: List[Digraph] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.node_by_id = {}
        self.usable_by_link = {}

    def get_definitions(self, content_type: TopLevelDisplayedContent) -> Sequence[WebPage]:
        """returns the definitions of `content_type`"""
        return getattr(self, f"{content_type.name.lower()}_defs")

    def _set_parents(self):
        """ set the parents in all objects """
        for obj in self.all_objects():
            for child in obj.children():
                child.parent = obj

    @property
    def basicfunction_defs(self) -> List[BasicFunction]:
        """collect all callables from libraries"""
        return sum((lib.basicfunctions for lib in self.library_defs), [])

    @property
    def module_defs(self) -> List[Module]:
        """collect all basic modules from libraries"""
        return sum((lib.modules for lib in self.library_defs), [])

    @property
    def pythonmodule_defs(self) -> List[PythonModule]:
        """collect all python modules from libraries"""
        return sum((lib.modules for lib in self.pythonlibrary_defs), [])

    def by_content_type(self, *content_type_class):
        """returns as iterator for all instances of `content_type_class`"""
        return \
            [obj for obj in self.all_objects()
             if isinstance(obj, tuple(content_type_class))]

    @property
    def embeddedqueries(self) -> Iterable[EmbeddedQuery]:
        """ collect all EmbeddedQuery objects """
        return self.by_content_type(EmbeddedQuery)

    @property
    def commanders(self):
        """ collect all AbstractCommander objects"""
        return self.by_content_type(AbstractCommander)

    @property
    def eventlisteners(self):
        """ collect all EventListener objects"""
        return self.by_content_type(EventListener)

    def children(self):
        return \
            chain(
                self.table_defs,
                self.view_defs,
                self.query_defs,
                self.form_defs,
                self.report_defs,
                self.library_defs,
                self.pythonlibrary_defs,
                self.textdocument_defs,
            )

    def _set_obj_ids(self) -> None:
        """ numbers all contained objects """
        for index, obj in zip(itertools.count(), self.all_objects()):
            obj.obj_id = str(index)

    def _create_index(self) -> None:
        """ make an index of linkable objects """
        for content in self.all_objects():
            self.node_by_id[content.obj_id] = content
            if isinstance(content, Usable):
                content = cast(Node, content)
                self.usable_by_link[content.identifier] = content

    def prepare_indexed_tree(self) -> None:
        """Setup for dependency search"""
        self._set_parents()
        self._set_obj_ids()
        self._create_index()

    @property
    def all_active_users(self) -> Iterable[User]:
        """ returns all User objects with a link set from the tree """
        # exclude tokens in Modules
        # pylint:disable=no-member

        return \
            (obj for obj in self.by_content_type(User)
                if obj.link and not (isinstance(obj.parent, Module) and isinstance(obj, Token)))
