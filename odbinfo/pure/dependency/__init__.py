" Dependency searcher for metadata "

import logging
from functools import partial
from typing import Iterable, Sequence

from odbinfo.pure.datatype import (BasicCall, BasicFunction, Commander,
                                   DatabaseDisplay, EmbeddedQuery,
                                   EventListener, Identifier, Key, Metadata,
                                   Module, Table, TextDocument, Token, WebPage,
                                   content_type)
from odbinfo.pure.datatype.base import Usable
from odbinfo.pure.dependency.searchexec import (
    _link_name_tokens, rewrite_module_callable_links,
    search_callable_in_callable, search_string_refs_in_callables)
from odbinfo.pure.dependency.searchtabular import *
from odbinfo.pure.dependency.searchui import *
from odbinfo.pure.util import timed


@timed("Search dependencies", indent=4)
def search_dependencies(metadata: Metadata):
    " dependency search in `metadata`"
    search_basicfunction_in_eventlistener(metadata.basicfunction_defs(),
                                          metadata.eventlisteners())
    search_tables_in_tables(metadata.table_defs)
    search_callable_in_callable(metadata.basicfunction_defs())
    search_string_refs_in_callables(metadata.table_defs,
                                    metadata.basicfunction_defs())
    search_string_refs_in_callables(metadata.view_defs,
                                    metadata.basicfunction_defs())
    search_string_refs_in_callables(metadata.query_defs,
                                    metadata.basicfunction_defs())
    search_string_refs_in_callables(metadata.report_defs,
                                    metadata.basicfunction_defs())
    search_string_refs_in_callables(metadata.textdocument_defs,
                                    metadata.basicfunction_defs())

    search_deps_in_queries(metadata.table_defs,
                           metadata.query_defs)
    search_deps_in_queries(metadata.view_defs,
                           metadata.query_defs)
    search_deps_in_queries(metadata.query_defs,
                           metadata.query_defs)
    search_deps_in_queries(metadata.table_defs,
                           metadata.view_defs)
    search_deps_in_queries(metadata.view_defs,
                           metadata.view_defs)
    search_deps_in_queries(metadata.table_defs,
                           metadata.embeddedquery_defs())
    search_deps_in_queries(metadata.view_defs,
                           metadata.embeddedquery_defs())
    search_deps_in_queries(metadata.query_defs,
                           metadata.embeddedquery_defs())
    search_deps_in_commander(metadata.table_defs,
                             metadata.commanders())
    search_deps_in_commander(metadata.view_defs,
                             metadata.commanders())
    search_deps_in_commander(metadata.query_defs,
                             metadata.commanders())
    search_deps_in_documents(metadata.table_defs,
                             metadata.textdocument_defs)
    search_deps_in_documents(metadata.view_defs,
                             metadata.textdocument_defs)
    search_deps_in_documents(
        metadata.query_defs, metadata.textdocument_defs)
    rewrite_module_callable_links(metadata.module_defs())