" Metadata class "
from dataclasses import dataclass, field
from itertools import starmap
from typing import List

from odbinfo.pure.datatype.base import PageOwner, UseCase, get_content_type
from odbinfo.pure.datatype.exec import (BasicFunction, Library, Module,
                                        PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import Query, Table, View
from odbinfo.pure.datatype.ui import Form, Report, SubForm, TextDocument

METADATA_CONTENT = ["tables",
                    "queries",
                    "views",
                    "forms",
                    "reports",
                    "basicfunctions",
                    "modules",
                    "libraries",
                    "pythonlibraries",
                    "pymodules",
                    "textdocuments"]

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
    textdocuments: List[TextDocument]
    use_cases: List[UseCase] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.index = {}

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
            self.textdocuments

        )

    def set_obj_ids(self) -> None:
        " numbers all contained objects "
        all_objs = self.all_objects()

        def set_id(vid, data):
            data.obj_id = str(vid)

        list(starmap(set_id, zip(range(len(all_objs)), all_objs)))

    def create_index(self) -> None:
        " make an index of linkable objects "
        for content in self.all_objects():
            if isinstance(content, PageOwner):
                content_type = get_content_type(content)
                # pylint:disable=no-member
                self.index[(content_type, content.title)] = content
