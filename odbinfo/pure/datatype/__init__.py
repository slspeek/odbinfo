""" Defines the main datatype MetaData """
from dataclasses import dataclass, field
from itertools import starmap
from typing import List, Optional, Sequence, Union, cast

from odbinfo.pure.datatype.base import (DataObject, Identifier, LinkedString,
                                        Token, UseCase, get_identifier)
from odbinfo.pure.datatype.exec import (BasicCall, BasicFunction, Library,
                                        Module, PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import (Column, Index, Key, Query,
                                           QueryColumn, Table, View)
from odbinfo.pure.datatype.ui import (CommandDriven, Control, DatabaseDisplay,
                                      EventListener, Form, Grid, ListBox,
                                      Report, SubForm, TextDocument)


# pylint: disable=too-many-instance-attributes
@dataclass
class Metadata(DataObject):
    """ Collector class for all metadata read from the odb-file """
    tables: List[Table]
    views: List[View]
    queries: List[Query]
    forms: List[Form]
    reports: List[Report]
    libraries: List[Library]
    pythonlibraries: List[PythonLibrary]
    documents: List[TextDocument]
    use_cases: List[UseCase] = field(init=False, default_factory=list)

    def basicfunctions(self) -> List[BasicFunction]:
        "collect all callables from libraries"
        result = []
        for lib in self.libraries:
            for module in lib.modules:
                result.extend(module.callables)
        return result

    def modules(self) -> List[Module]:
        "collect all basic modules from libraries"
        result = []
        for lib in self.libraries:
            result.extend(lib.modules)
        return result

    def pymodules(self) -> List[PythonModule]:
        "collect all python modules from libraries"
        result = []
        for lib in self.pythonlibraries:
            result.extend(lib.modules)
        return result

    def subforms(self) -> List[SubForm]:
        " collect all subforms from the forms and subforms "
        def collect_subforms(subform: SubForm) -> List[SubForm]:
            result = [subform]
            result.extend(sum([collect_subforms(sf)
                          for sf in subform.subforms], []))
            return result

        def collect_subforms_from_form(form: Form) -> List[SubForm]:
            return sum([collect_subforms(sf) for sf in form.subforms], [])

        return sum([collect_subforms_from_form(f) for f in self.forms], [])

    def children(self) -> List[DataObject]:
        return (

            cast(List['DataObject'], self.tables) +
            cast(List['DataObject'], self.views) +
            cast(List['DataObject'], self.queries) +
            cast(List['DataObject'], self.forms) +
            cast(List['DataObject'], self.reports) +
            cast(List['DataObject'], self.libraries) +
            cast(List['DataObject'], self.pythonlibraries) +
            cast(List['DataObject'], self.documents)

        )

    def set_obj_ids(self) -> None:
        " numbers all contained objects "
        all_objs = self.all_objects()

        def set_id(vid, data: DataObject):
            data.obj_id = vid

        list(starmap(set_id, zip(range(len(all_objs)), all_objs)))


__all__ = [
    "BasicCall",
    "BasicFunction",
    "Column",
    "CommandDriven",
    "Control",
    "DatabaseDisplay",
    "EventListener",
    "get_identifier",
    "Grid",
    "Identifier",
    "Index",
    "Key",
    "LinkedString",
    "ListBox",
    "Metadata",
    "Query",
    "QueryColumn",
    "Table",
    "UseCase",
    "View"
]
