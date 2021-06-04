""" Core module """
from functools import partial
from typing import Sequence, Union

from odbinfo.pure.datatype import (Control, Form, Grid, Library, Metadata,
                                   Module, Query, SubForm)
from odbinfo.pure.dependency import search_dependencies
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.parser.sql import parse


def _process_library(library: Library) -> None:
    def parse_module(module: Module) -> None:
        # print("parsing: " + module.source)
        module.tokens =\
            get_basic_tokens(module.source)
        module.callables =\
            scan_basic(module.tokens, library.name, module.name)
        module.name_indexes =\
            list(map(lambda c: c.name_token_index, module.callables))

    list(map(parse_module, library.modules))


def _process_libraries(libraries: Sequence[Library]) -> None:
    list(map(_process_library, libraries))


def _process_query(query: Query) -> None:
    query.table_tokens, query.tokens = parse(query.command)


def set_depth(depth: int, subform: SubForm) -> None:
    " sets depth recursively in `subform`"
    subform.depth = depth
    list(map(partial(set_depth, depth + 1), subform.subforms))


def height(subform: SubForm) -> int:
    " max path length to a leaf subform "
    if subform.subforms:
        return max(height(sf) for sf in subform.subforms) + 1
    return 0


def set_form_height(form: Form) -> None:
    " set the max height into the `form` "
    form.height = max([height(sf) for sf in form.subforms], default=0)


def process_subform(subform: SubForm) -> None:
    " simplifies control.type for all (nested) controls "
    def process_control(control: Union[Control, Grid]) -> None:
        if isinstance(control, Grid):
            return
        control.type = control.type.split(".")[-1]
    list(map(process_control, subform.controls))
    list(map(process_subform, subform.subforms))


def process_form(form: Form) -> None:
    " calculate depth for its subforms "
    list(map(partial(set_depth, 0), form.subforms))
    list(map(process_subform, form.subforms))
    set_form_height(form)


def process_metadata(metadata: Metadata) -> None:
    " preprocessing of the data before it is send to hugo "
    _process_libraries(metadata.libraries)
    list(map(_process_query, metadata.queries))
    list(map(_process_query, metadata.views))
    list(map(process_form, metadata.forms))
    metadata.use_cases = search_dependencies(metadata)
