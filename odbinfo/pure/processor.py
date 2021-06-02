""" Core module """
from functools import partial
from typing import Sequence

from odbinfo.pure.datatype import Form, Library, Module, Query, SubForm
from odbinfo.pure.dependency import search_dependencies
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.parser.sql import parse


def _process_library(library: Library):
    def parse_module(module: Module):
        # print("parsing: " + module.source)
        module.tokens =\
            get_basic_tokens(module.source)
        module.callables =\
            scan_basic(module.tokens, library.name, module.name)
        module.name_indexes =\
            list(map(lambda c: c.name_token_index, module.callables))

    list(map(parse_module, library.modules))


def _process_libraries(libraries: Sequence[Library]):
    list(map(_process_library, libraries))


def _process_query(query: Query):
    query.table_tokens, query.tokens = parse(query.command)


def set_depth(depth: int, subform: SubForm) -> None:
    " sets depth recursively in `subform`"
    subform.depth = depth
    list(map(partial(set_depth, depth + 1), subform.subforms))


def process_form(form: Form) -> None:
    " calculate depth for its subforms "
    list(map(partial(set_depth, 0), form.subforms))


def process_metadata(metadata):
    " preprocessing of the data before it is send to hugo "
    _process_libraries(metadata.libraries)
    list(map(_process_query, metadata.queries))
    list(map(_process_query, metadata.views))
    list(map(process_form, metadata.forms))
    metadata.use_cases = search_dependencies(metadata)
