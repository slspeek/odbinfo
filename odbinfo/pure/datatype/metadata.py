" Metadata class "
from dataclasses import dataclass, field
from itertools import starmap
from typing import List

from odbinfo.pure.datatype.base import PageOwner, UseCase
from odbinfo.pure.datatype.exec import (BasicFunction, Library, Module,
                                        PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import Query, Table, View
from odbinfo.pure.datatype.ui import Form, Report, SubForm, TextDocument


# pylint: disable=too-many-instance-attributes
@dataclass
class Metadata(PageOwner):
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

    def children(self):
        return (

            self.tables +
            self.views +
            self.queries +
            self.forms +
            self.reports +
            self.libraries +
            self.pythonlibraries +
            self.documents

        )

    def set_obj_ids(self) -> None:
        " numbers all contained objects "
        all_objs = self.all_objects()

        def set_id(vid, data):
            data.obj_id = str(vid)
            # print(data.__class__.__name__, vid)

        list(starmap(set_id, zip(range(len(all_objs)), all_objs)))
