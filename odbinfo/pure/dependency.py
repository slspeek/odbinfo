" Dependency searcher for metadata "
import logging
from functools import partial
from typing import Iterable, Sequence

from odbinfo.pure.datatype import (BasicCall, BasicFunction, Commander,
                                   DatabaseDisplay, EmbeddedQuery,
                                   EventListener, Identifier, Key, Metadata,
                                   Module, PageOwner, Table, TextDocument,
                                   Token, content_type, get_identifier)
from odbinfo.pure.datatype.base import Usable
from odbinfo.pure.util import timed

logger = logging.getLogger(__name__)


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
    # search_deps_in_queries(metadata.view_defs,
    #                        metadata.embeddedquery_defs())
    # search_deps_in_queries(metadata.query_defs,
    #                        metadata.embeddedquery_defs())
    search_deps_in_commander(metadata.table_defs,
                             metadata.report_defs)
    search_deps_in_commander(metadata.view_defs,
                             metadata.report_defs)
    search_deps_in_commander(metadata.query_defs,
                             metadata.report_defs)
    search_deps_in_commander(
        metadata.table_defs, metadata.subform_defs())
    search_deps_in_commander(metadata.view_defs, metadata.subform_defs())
    search_deps_in_commander(metadata.query_defs,
                             metadata.subform_defs())
    search_deps_in_documents(metadata.table_defs,
                             metadata.textdocument_defs)
    search_deps_in_documents(metadata.view_defs,
                             metadata.textdocument_defs)
    search_deps_in_documents(
        metadata.query_defs, metadata.textdocument_defs)
    rewrite_module_callable_links(metadata.module_defs())

#
# BasicFunction in BasicFunction
#


def _rewrite_module_token_links(modules):
    " scan module tokens for links"
    # process module source tokens to support callable links at module level
    # e.g /Lib1.Mod1/#macro
    # By rewriting Identifier(type="BasicFunction" local_id="call.Mod1.Lib1")
    # to Identifier("Module", "Mod1.Lib1", bookmark="call")
    # module_index = {}
    # for module in modules:
    #     module_index[(module.name, module.library)] = module

    def rewrite_module(module: Module):
        def rewrite_link(link: Identifier):
            if not link.content_type == content_type(BasicFunction):
                return link
            lmacro, lmodule, llib = link.local_id.split('.')
            return Identifier(content_type(Module), f"{lmodule}.{llib}", lmacro)

        def copy_links(function):
            for token in function.tokens:
                module_token = module.tokens[token.index]
                if token.link:
                    module_token.link = rewrite_link(token.link)

        for function in module.callables:
            copy_links(function)

    for module in modules:
        rewrite_module(module)


def _link_name_tokens(module: Module):
    def _link_name(index: int, acallable: BasicFunction):
        link_token(module.tokens[index], acallable)
    for name_index, acallable in zip(module.name_indexes, module.callables):
        _link_name(name_index, acallable)


def rewrite_module_callable_links(module_seq: Sequence[Module]) -> None:
    """ links to callables are rewritten to links to callables in
        modules (using #bookmarks)"""
    _rewrite_module_token_links(module_seq)


def search_callable_in_callable(callables: Sequence[BasicFunction]) -> None:
    """ dependency search amoung the basic callables and linking the
    parsed tokens to the targets
    the callable tokens are linked during search
    the module tokens links are rewritten afterwards
    find calls from one to another """

    def search_in_one(caller: BasicFunction):
        # caller's module
        def filter_own_module(call: BasicFunction):
            return (call.module == caller.module
                    and call.library == caller.library)

        # callables in own library
        def filter_own_library(call: BasicFunction):
            return (not (call.module == caller.module)
                    and call.library == caller.library)

        # callables in other libraries
        def filter_other_library(call: BasicFunction):
            return not call.library == caller.library

        # the order is crucial as it represents scope in OOBasic
        candidates = (list(filter(filter_own_module, callables))
                      + list(filter(filter_own_library, callables))
                      + list(filter(filter_other_library, callables)))
        consider_caller = partial(consider, caller)
        for candidate in candidates:
            consider_caller(candidate)
    for acallable in callables:
        search_in_one(acallable)


def link_token(token: Token, referand):
    "link `token` to `referand`"

    if token.link:
        # pylint:disable=logging-too-many-args
        logger.warning(
            "Replacing link in token: %s (link=%s:%s) with %s:%s",
            token.title,
            token.link.content_type,
            token.link.local_id,
            referand.content_type(),
            referand.name)
    token.link = get_identifier(referand)


def consider(caller: BasicFunction, candidate_callee: BasicFunction) -> None:
    " find calls in `caller` to `candidate_callee`"

    def match_and_not_linked(acall: BasicCall):
        if acall.module_token:
            if acall.module_token.text.upper() != candidate_callee.module.upper():
                return False, acall

        return (acall.name_token.text.upper() == candidate_callee.name.upper()
                and acall.name_token.link is None, acall)

    def process_match(acall: BasicCall):
        link_token(acall.name_token, candidate_callee)

    for match, ntoken in map(match_and_not_linked, caller.calls):
        if match:
            process_match(ntoken)


#
# Tables, Views, Queries, Reports, TextDocument in BasicFunction
#


def search_string_refs_in_callables(dataobjects: Sequence[PageOwner],
                                    callables: Sequence[BasicFunction]) -> None:
    """ search for references to table, views, queries or reports
        in callable string literals """
    def search_refs_in_one(acallable: BasicFunction) -> None:
        def ref_in_one(dataobject: PageOwner) -> None:
            def compare_ref(string_token: Token) -> None:
                if dataobject.users_match(string_token.text[1:-1]):
                    link_token(string_token, dataobject)
            for stoken in acallable.strings:
                compare_ref(stoken)
        for obj in dataobjects:
            ref_in_one(obj)
    for acallable in callables:
        search_refs_in_one(acallable)


#
# BasicFunction in EventListener
#

def search_basicfunction_in_eventlistener(funcs: Iterable[BasicFunction],
                                          eventlisteners: Iterable[EventListener]):
    "searches for references to basic macros in eventlisteners"
    for evl in eventlisteners:
        for func in funcs:
            if f"{func.library}.{func.module}.{func.name}" == evl.parsescript():
                evl.link = get_identifier(func)


#
# dataobject in Queries
#


def search_deps_in_queries(dataobjects: Sequence[Usable],
                           queries: Iterable[EmbeddedQuery]) -> None:
    " find uses of `dataobjects` (Table, View, Query) in `queries` "
    def find_tabulars_in_query(query: EmbeddedQuery) -> None:
        " find tabular uses in `query` "
        def find_tabular_in_query(usable: Usable) -> None:
            def find_tabular_in_token(token: Token) -> None:
                if usable.users_match(token.text[1:-1]):  # type: ignore
                    link_token(token, usable)
            for token in query.table_tokens:
                find_tabular_in_token(token)
        for tabular in dataobjects:
            find_tabular_in_query(tabular)
    for query in queries:
        find_tabulars_in_query(query)

#
# DataObject (query, view, table) in Report, SubForm
#


# pylint:disable=line-too-long

def search_deps_in_commander(dataobjects: Sequence[PageOwner],
                             commander_seq: Sequence[Commander]) -> None:
    " find uses of dataobject in report"
    def find_deps_in_commander(commander: Commander) -> None:
        " find dependency uses in `report` "
        def match_one_dep(dependency: PageOwner) -> None:
            if (not commander.get_commandtype() == "command"  # no matching of embedded
                # queries (COMMAND)
                    and dependency.users_match(commander.get_command())):
                commander.link = get_identifier(dependency)
        for obj in dataobjects:
            match_one_dep(obj)
    for commander in commander_seq:
        find_deps_in_commander(commander)


def search_deps_in_documents(dataobjects: Sequence[PageOwner],
                             documents: Sequence[TextDocument]) -> None:
    " find uses of dataobject in document"
    def find_deps_in_doc(document: TextDocument) -> None:

        def find_one_dep(dependency: PageOwner) -> None:

            def find_in_databasedisplay(display: DatabaseDisplay) -> None:
                if dependency.users_match(display.table):
                    display.link = get_identifier(dependency)

            for field in document.fields:
                find_in_databasedisplay(field)
        for obj in dataobjects:
            find_one_dep(obj)
    for doc in documents:
        find_deps_in_doc(doc)


#
# Tables in Tables
#


def search_tables_in_tables(tables: Sequence[Table]) -> None:
    " search for foreign key references amoung tables "
    def search_in_one_table(atable: Table) -> None:

        def search_one_key(key: Key) -> None:

            def match_table(othertable: Table) -> None:
                if othertable.users_match(key.referenced_table):
                    key.link = get_identifier(othertable)
            for obj in tables:
                match_table(obj)
        for key in atable.keys:
            search_one_key(key)
    for table in tables:
        search_in_one_table(table)
