" Metadata class "
from dataclasses import dataclass, field
from itertools import starmap
from typing import List

from odbinfo.pure.datatype.base import PageOwner, UseCase
from odbinfo.pure.datatype.exec import (BasicFunction, Library, Module,
                                        PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import Query, Table, View
from odbinfo.pure.datatype.ui import Form, Report, SubForm, TextDocument

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
class Metadata(PageOwner):

    """ Collector class for all metadata read from the odb-file """
    table_defs: List[Table]
    view_defs: List[View]
    query_defs: List[Query]
    form_defs: List[Form]
    report_defs: List[Report]
    library_defs: List[Library]
    pythonlibrary_defs: List[PythonLibrary]
    textdocument_defs: List[TextDocument]
    use_cases: List[UseCase] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.index = {}

    def basicfunction_defs(self) -> List[BasicFunction]:
        "collect all callables from libraries"
        result = []
        for lib in self.library_defs:
            for module in lib.modules:
                result.extend(module.callables)
        return result

    def module_defs(self) -> List[Module]:
        "collect all basic modules from libraries"
        result = []
        for lib in self.library_defs:
            result.extend(lib.modules)
        return result

    def pythonmodule_defs(self) -> List[PythonModule]:
        "collect all python modules from libraries"
        result = []
        for lib in self.pythonlibrary_defs:
            result.extend(lib.modules)
        return result

    def subform_defs(self) -> List[SubForm]:
        " collect all subforms from the forms and subforms "
        def collect_subforms(subform: SubForm) -> List[SubForm]:
            result = [subform]
            result.extend(sum([collect_subforms(sf)
                          for sf in subform.subforms], []))
            return result

        def collect_subforms_from_form(form: Form) -> List[SubForm]:
            return sum([collect_subforms(sf) for sf in form.subforms], [])

        return sum([collect_subforms_from_form(f) for f in self.form_defs], [])

    def children(self):
        return (

            self.table_defs +
            self.view_defs +
            self.query_defs +
            self.form_defs +
            self.report_defs +
            self.library_defs +
            self.pythonlibrary_defs +
            self.textdocument_defs

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
                # pylint:disable=no-member
                self.index[(content.type_name(), content.title)] = content
