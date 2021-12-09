""" Dependency searcher for metadata """

from odbinfo.pure.datatype import (EmbeddedQuery, Key, Metadata, Query, Report,
                                   Table, TextDocument, View)
from odbinfo.pure.dependency.searchexec import (
    search_callable_in_callable, search_string_refs_in_callables)
from odbinfo.pure.dependency.searchtabular import (search_deps_in_queries,
                                                   search_tables_in_keys)
from odbinfo.pure.dependency.searchui import (
    search_basicfunction_in_eventlistener, search_deps_in_commander,
    search_deps_in_documents)
from odbinfo.pure.dependency.util import link_user_to_usuable
from odbinfo.pure.util import timed

__all__ = [
    "search_dependencies",
    "link_user_to_usuable"
]


@timed("Search dependencies", indent=4)
def search_dependencies(metadata: Metadata) -> None:
    """ dependency search in `metadata`"""
    search_basicfunction_in_eventlistener(metadata.basicfunction_defs,
                                          metadata.eventlisteners)
    search_tables_in_keys(metadata.table_defs, metadata.by_content_type(Key))
    search_callable_in_callable(metadata.basicfunction_defs)
    search_string_refs_in_callables(metadata.by_content_type(Table,
                                                             Query,
                                                             View,
                                                             Report,
                                                             TextDocument),
                                    metadata.basicfunction_defs)
    search_deps_in_queries(metadata.by_content_type(Table, View),
                           metadata.by_content_type(View))
    search_deps_in_queries(metadata.by_content_type(Table, Query, View),
                           metadata.by_content_type(Query, EmbeddedQuery))
    search_deps_in_commander(metadata.by_content_type(Table, Query, View),
                             metadata.commanders)
    search_deps_in_documents(metadata.by_content_type(Table, Query, View),
                             metadata.textdocument_defs)
