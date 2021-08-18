" Metadata class "
from dataclasses import dataclass, field
from functools import partial
from itertools import starmap
from typing import List

from graphviz import Digraph

from odbinfo.pure.datatype.base import PageOwner, User
from odbinfo.pure.datatype.exec import (BasicFunction, Library, Module,
                                        PythonLibrary, PythonModule)
from odbinfo.pure.datatype.tabular import EmbeddedQuery, Query, Table, View
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
    # use_cases: List[UseCase] = field(init=False, default_factory=list)
    graphs: List[Digraph] = field(init=False, default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.index = {}

    def build_parent_index(self):
        " set the parents in all objects "
        for obj in self.all_objects():
            for child in obj.children():
                child.parent = obj

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

    def embeddedquery_defs(self) -> List[EmbeddedQuery]:
        " collect all EmbeddedQuery objects "
        return \
            [obj for obj in self.all_objects() if obj.__class__ == EmbeddedQuery]

    def children(self):
        return (

            self.table_defs
            + self.view_defs
            + self.query_defs
            + self.form_defs
            + self.report_defs
            + self.library_defs
            + self.pythonlibrary_defs
            + self.textdocument_defs

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
            self.index[(content.content_type(), content.title)] = content

    def set_titles(self):
        " set the titles so that they are unique within their content_type "
        for content in self.all_objects():
            # pylint:disable=no-member
            content.set_title()

    def verify_titles_unique_in_kind(self):
        " verify that titles are unique within their kind"
        def _print_doubles(titles_minus):

            def select_by_title(title, cand):
                return title == cand

            for title in titles_minus:
                if len(list(filter(partial(select_by_title, title), titles_minus))) > 1:
                    print("Double: ", title)

        all_objs = self.all_objects()
        title_list = list(
            map(lambda x: f"{x.content_type()}:{x.title}", all_objs))
        title_set = set(title_list)
        if not len(all_objs) == len(title_set):
            _print_doubles(title_list)
        assert len(all_objs) == len(title_set)

    def all_active_users(self):
        " returns all User objects with a link set from the tree "
        # exclude tokens in Modules
        # pylint:disable=no-member

        return \
            [obj for obj in self.all_objects() if isinstance(obj, User)
             and obj.link and not isinstance(obj.parent, Module)]
