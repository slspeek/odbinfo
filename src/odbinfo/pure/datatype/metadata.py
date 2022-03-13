""" Metadata class
Contains all the metadata read from the odb zipfile or retrieved from staroffice.
Like Tables, Views,  Queries, Forms, Reports and BasicFunctions.
"""
import itertools
from dataclasses import dataclass, field
from enum import Enum
from itertools import chain
from typing import Iterable, List, Optional, Sequence, cast

from graphviz import Digraph

from odbinfo.pure.datatype.base import BasicToken, Node, Usable, User, WebPage
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)
from odbinfo.pure.datatype.tabular import Query, Table, View
from odbinfo.pure.datatype.ui import Form, Report, TextDocument


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
    """ Collector class for all metadata read from the odb-file or retrieved from staroffice"""
    table_defs: List[Table]
    view_defs: List[View]
    query_defs: List[Query]
    form_defs: List[Form]
    report_defs: List[Report]
    library_defs: List[Library]
    pythonlibrary_defs: List[PythonLibrary]
    textdocument_defs: List[TextDocument]
    graph: Optional[Digraph] = field(init=False, default=None)

    def __post_init__(self):
        super().__post_init__()
        self.node_by_id = {}
        self.usable_by_link = {}

    def get_definitions(
            self, content_type: TopLevelDisplayedContent) -> Sequence[WebPage]:
        """ Returns the definitions of `content_type`
            Another way of calling table_defs, form_defs etc.
        """
        return getattr(self, f"{content_type.name.lower()}_defs")

    def _set_parents(self):
        """ Sets the parents in all objects """
        for obj in self.all_objects():
            for child in obj.children():
                child.parent = obj

    @property
    def basicfunction_defs(self) -> List[BasicFunction]:
        """ Returns a list of all basic functions """
        return sum((lib.basicfunctions for lib in self.library_defs), [])

    @property
    def module_defs(self) -> List[Module]:
        """ Returns a list of all basic modules """
        return sum((lib.modules for lib in self.library_defs), [])

    @property
    def pythonmodule_defs(self) -> List[PythonModule]:
        """ Returns a list of all python modules """
        return sum((lib.modules for lib in self.pythonlibrary_defs), [])

    def by_content_type(self, *content_type_class):
        """ Returns as iterator for all instances of the `content_type_class` arguments """
        return \
            [obj for obj in self.all_objects()
             if isinstance(obj, tuple(content_type_class))]

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
        """ Numbers all contained objects """
        for index, obj in zip(itertools.count(), self.all_objects()):
            obj.obj_id = str(index)

    def _create_index(self) -> None:
        """ Creates two indexes
         one by obj_id and one by identifier.
         """
        for content in self.all_objects():
            # pylint:disable=no-member
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
    def actual_users(self) -> Iterable[User]:
        """ Returns an iterator on all User objects with their link set """
        # exclude tokens in Modules, the ones from the BasicFunctions suffice
        # pylint:disable=no-member
        return \
            (obj for obj in self.by_content_type(User)
             if obj.link and not (isinstance(obj.parent, Module) and isinstance(obj, BasicToken)))
