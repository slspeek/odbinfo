""" Dependency searcher for metadata """

from odbinfo.pure.datatype import (EmbeddedQuery, Key, Metadata, Query, Report,
                                   Table, TextDocument, View)
from odbinfo.pure.dependency.searchexec import (
    search_callable_in_callable, search_string_refs_in_callables)
from odbinfo.pure.dependency.searchui import (
    search_basicfunction_in_eventlistener, search_deps_in_documents)
from odbinfo.pure.dependency.util import search_combinations
from odbinfo.pure.util import timed

__all__ = [
    "search_dependencies",
]


@timed("Search dependencies", indent=4)
def search_dependencies(metadata: Metadata) -> None:
    """ dependency search in `metadata`"""
    search_basicfunction_in_eventlistener(metadata.basicfunction_defs,
                                          metadata.eventlisteners)
    search_callable_in_callable(metadata.basicfunction_defs)
    search_string_refs_in_callables(metadata.by_content_type(Table,
                                                             Query,
                                                             View,
                                                             Report,
                                                             TextDocument),
                                    metadata.basicfunction_defs)

    search_combinations(metadata.by_content_type(Key), metadata.table_defs)
    search_combinations(metadata.by_content_type(View),
                        metadata.by_content_type(Table, View))
    search_combinations(metadata.by_content_type(Query, EmbeddedQuery),
                        metadata.by_content_type(Table, Query, View))
    search_combinations(metadata.commanders,
                        metadata.by_content_type(Table, Query, View))
    search_deps_in_documents(metadata.by_content_type(Table, Query, View),
                             metadata.textdocument_defs)