""" Core module """
from odbinfo.pure.datatype import Library, Module, Query
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


def _process_libraries(libraries: [Library]):
    list(map(_process_library, libraries))


def _process_query(query: Query):
    query.table_tokens, query.tokens = parse(query.command)


def process_metadata(metadata):
    " preprocessing of the data before it is send to hugo "
    _process_libraries(metadata.libraries)
    list(map(_process_query, metadata.queries))
    list(map(_process_query, metadata.views))
    metadata.use_cases = search_dependencies(metadata)
