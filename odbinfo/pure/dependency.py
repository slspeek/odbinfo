" Dependency searcher for metadata "
import logging
from functools import partial
from typing import List, Optional, Sequence, Tuple, cast

from odbinfo.pure.datatype import (BasicCall, BasicFunction, CommandDriven,
                                   DatabaseDisplay, Identifier, Key, Metadata,
                                   Module, Node, PageOwner, Query, Table,
                                   TextDocument, Token, UseCase,
                                   get_identifier, use_case)

logger = logging.getLogger(__name__)


def _subforms(metadata: Metadata) -> List[Tuple[PageOwner, CommandDriven]]:
    result = []
    for form in metadata.form_defs:
        result += [(form, sf) for sf in form.all_subforms()]
    return cast(List[Tuple[PageOwner, CommandDriven]], result)


def search_dependencies(metadata: Metadata) -> List[UseCase]:
    " dependency search in `metadata`"
    usecases = (
        search_tables_in_tables(metadata.table_defs)
        + search_callable_in_callable(metadata.basicfunction_defs())
        + search_string_refs_in_callables(metadata.table_defs,
                                          metadata.basicfunction_defs())
        + search_string_refs_in_callables(metadata.view_defs,
                                          metadata.basicfunction_defs())
        + search_string_refs_in_callables(metadata.query_defs,
                                          metadata.basicfunction_defs())
        + search_string_refs_in_callables(metadata.report_defs,
                                          metadata.basicfunction_defs())
        + search_string_refs_in_callables(metadata.textdocument_defs,
                                          metadata.basicfunction_defs())

        + search_deps_in_queries(metadata.table_defs,
                                 metadata.query_defs)
        + search_deps_in_queries(metadata.view_defs,
                                 metadata.query_defs)
        + search_deps_in_queries(metadata.query_defs,
                                 metadata.query_defs)
        + search_deps_in_queries(metadata.table_defs,
                                 metadata.view_defs)
        + search_deps_in_queries(metadata.view_defs,
                                 metadata.view_defs)
        + search_deps_in_commanddriven(metadata.table_defs,
                                       list(zip(metadata.report_defs,
                                                metadata.report_defs)))
        + search_deps_in_commanddriven(metadata.view_defs,
                                       list(zip(metadata.report_defs,
                                                metadata.report_defs)))
        + search_deps_in_commanddriven(metadata.query_defs,
                                       list(zip(metadata.report_defs,
                                                metadata.report_defs)))
        + search_deps_in_commanddriven(
            metadata.table_defs, _subforms(metadata))
        + search_deps_in_commanddriven(metadata.view_defs, _subforms(metadata))
        + search_deps_in_commanddriven(metadata.query_defs,
                                       _subforms(metadata))
        + search_deps_in_documents(metadata.table_defs,
                                   metadata.textdocument_defs)
        + search_deps_in_documents(metadata.view_defs,
                                   metadata.textdocument_defs)
        + search_deps_in_documents(
            metadata.query_defs, metadata.textdocument_defs)
    )
    rewrite_module_callable_links(metadata.module_defs())
    return usecases

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
            if not link.object_type == "basicfunction":
                return link
            lmacro, lmodule, llib = link.local_id.split('.')
            return Identifier("modules", f"{lmodule}.{llib}", lmacro)

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
    for module in module_seq:
        _link_name_tokens(module)


def search_callable_in_callable(callables: Sequence[BasicFunction]) -> List[UseCase]:
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
        return sum(map(consider_caller, candidates), [])

    return sum(map(search_in_one, callables), [])


def link_token(token: Token, referand: PageOwner):
    "link `token` to `acallable`"
    if token.link:
        # pylint:disable=logging-too-many-args
        logger.warning(
            "Replacing link in token: {} (link={}:{}) with {}:{}",
            token.title,
            token.link.object_type,
            token.link.local_id,
            referand.type_name(),
            referand.name)
    token.link = get_identifier(referand)


def consider(caller: BasicFunction, candidate_callee: BasicFunction) -> List[UseCase]:
    " find calls in `caller` to `candidate_callee`"

    def match_and_not_linked(acall: BasicCall):
        if acall.module_token:
            if acall.module_token.text.upper() != candidate_callee.module.upper():
                return False, acall

        return (acall.name_token.text.upper() == candidate_callee.name.upper()
                and acall.name_token.link is None, acall)

    def process_match(acall: BasicCall):
        link_token(acall.name_token, candidate_callee)
        return use_case(
            caller,
            acall.name_token,
            candidate_callee,
            "invokes")

    use_cases = []
    for match, ntoken in map(match_and_not_linked, caller.calls):
        if match:
            use_cases.append(process_match(ntoken))
    return use_cases

#
# Tables, Views, Queries, Reports in BasicFunction
#


def search_string_refs_in_callables(dataobjects: Sequence[PageOwner],
                                    callables: Sequence[BasicFunction]) -> List[UseCase]:
    """ search for references to table, views, queries or reports
        in callable string literals """
    def search_refs_in_one(acallable: BasicFunction) -> List[UseCase]:
        def ref_in_one(dataobject: PageOwner) -> List[UseCase]:
            def compare_ref(string_token: Token) -> List[UseCase]:
                if dataobject.users_match(string_token.text[1:-1]):
                    link_token(string_token, dataobject)
                    return [use_case(acallable,
                                     string_token,
                                     dataobject,
                                     "string refers")]
                return []
            return sum(map(compare_ref, acallable.strings), [])
        return sum(map(ref_in_one, dataobjects), [])

    return sum(map(search_refs_in_one, callables), [])


#
# dataobject in Queries
#


def search_deps_in_queries(dataobjects: Sequence[PageOwner],
                           queries: Sequence[Query]) -> List[UseCase]:
    " find uses of dataobject in queries "
    def find_tables_in_query(query: Query) -> List[UseCase]:
        " find table uses in `query` "
        def find_table_in_query(page: PageOwner) -> List[UseCase]:
            def find_table_in_token(token: Token) -> List[UseCase]:
                use_cases = []
                if page.users_match(token.text[1:-1]):
                    link_token(token, page)
                    use_cases.append(use_case(query,
                                              token,
                                              page,
                                              "queries"))
                return use_cases

            return sum(map(find_table_in_token, query.table_tokens), [])
        return sum(map(find_table_in_query, dataobjects), [])

    return sum(map(find_tables_in_query, queries), [])

#
# DataObject (query, view, table) in Report, SubForm
#


PageCmd = Tuple[PageOwner, CommandDriven]

# pylint:disable=line-too-long

#


def search_deps_in_commanddriven(dataobjects: Sequence[PageOwner],
                                 reports: Sequence[Tuple[PageOwner, CommandDriven]]) -> List[UseCase]:
    " find uses of dataobject in report"
    def find_deps_in_report(report: Tuple[PageOwner, CommandDriven]) -> List[UseCase]:
        " find dependency uses in `report` "
        page, cmddriven = report

        def match_one_dep(dependency: PageOwner) -> Optional[UseCase]:
            if dependency.users_match(cmddriven.command):
                cmddriven.link = get_identifier(dependency)
                if isinstance(cmddriven, Node):
                    location = cast(Node, cmddriven)
                else:
                    location = page
                return use_case(page,
                                location,
                                dependency,
                                "queries")

            return None

        return [obj for obj in map(match_one_dep, dataobjects) if obj is not None]

    return sum(map(find_deps_in_report, reports), [])


def search_deps_in_documents(dataobjects: Sequence[PageOwner],
                             documents: Sequence[TextDocument]) -> List[UseCase]:
    " find uses of dataobject in document"
    def find_deps_in_doc(document: TextDocument) -> List[UseCase]:

        def find_one_dep(dependency: PageOwner) -> List[UseCase]:

            def find_in_databasedisplay(display: DatabaseDisplay) -> Optional[UseCase]:
                if dependency.users_match(display.table):
                    display.link = get_identifier(dependency)
                    return use_case(document,
                                    display,
                                    dependency,
                                    "queries")
                return None

            return [obj for obj in map(find_in_databasedisplay, document.fields)
                    if obj is not None]

        return sum(map(find_one_dep, dataobjects), [])

    return sum(map(find_deps_in_doc, documents), [])

#
# Tables in Tables
#


def search_tables_in_tables(tables: Sequence[Table]) -> List[UseCase]:
    " search for foreign key references amoung tables "
    def search_in_one_table(atable: Table) -> List[UseCase]:

        def search_one_key(key: Key) -> List[UseCase]:

            def match_table(othertable: Table) -> Optional[UseCase]:
                if othertable.users_match(key.referenced_table):
                    key.link = get_identifier(othertable)
                    return use_case(atable, key, othertable, "references")
                return None

            return [obj for obj in map(match_table, tables) if obj is not None]

        return sum([obj for obj in map(search_one_key, atable.keys) if obj is not None], [])

    return sum(map(search_in_one_table, tables), [])
