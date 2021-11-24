""" Metadata class """
import itertools
from dataclasses import dataclass, field
from itertools import chain
from typing import Iterable, List, cast

from graphviz import Digraph

from odbinfo.pure.datatype.base import Node, Usable, User, WebPage
from odbinfo.pure.datatype.exec import (BasicFunction, Library, Module,
                                        PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import EmbeddedQuery, Query, Table, View
from odbinfo.pure.datatype.ui import (AbstractCommander, EventListener, Form,
                                      Report, TextDocument)

METADATA_CONTENT = ["table",
                    "query",
                    "view",
                    "form",
                    "report",
                    "basicfunction",
                    "module",
                    "library",
                    "pythonlibrary",
                    "pythonmodule",
                    "textdocument"]

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
        self.index = {}
        self.usable_by_link = {}

    def build_parent_index(self):
        """ set the parents in all objects """
        for obj in self.all_objects():
            for child in obj.children():
                child.parent = obj

    def basicfunction_defs(self) -> List[BasicFunction]:
        """collect all callables from libraries"""
        result = []
        for lib in self.library_defs:
            for module in lib.modules:
                result.extend(module.callables)
        return result

    def module_defs(self) -> List[Module]:
        """collect all basic modules from libraries"""
        result = []
        for lib in self.library_defs:
            result.extend(lib.modules)
        return result

    def pythonmodule_defs(self) -> List[PythonModule]:
        """collect all python modules from libraries"""
        result = []
        for lib in self.pythonlibrary_defs:
            result.extend(lib.modules)
        return result

    def embeddedquery_defs(self) -> Iterable[EmbeddedQuery]:
        """ collect all EmbeddedQuery objects """
        return \
            (obj for obj in self.all_objects() if obj.__class__ == EmbeddedQuery)

    def commanders(self):
        """ collect all AbstractCommander objects"""
        return \
            (obj for obj in self.all_objects()
             if isinstance(obj, AbstractCommander))

    def eventlisteners(self):
        """ collect all EventListener objects"""
        return \
            (obj for obj in self.all_objects()
             if isinstance(obj, EventListener))

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

    def set_obj_ids(self) -> None:
        """ numbers all contained objects """
        for index, obj in zip(itertools.count(), self.all_objects()):
            obj.obj_id = str(index)

    def create_index(self) -> None:
        """ make an index of linkable objects """
        for content in self.all_objects():
            self.index[content.obj_id] = content
            if isinstance(content, Usable):
                content = cast(Node, content)
                self.usable_by_link[content.identifier] = content

    def all_active_users(self):
        """ returns all User objects with a link set from the tree """
        # exclude tokens in Modules
        # pylint:disable=no-member

        return \
            (obj for obj in self.all_objects() if isinstance(obj, User)
             and obj.link and not isinstance(obj.parent, Module))
