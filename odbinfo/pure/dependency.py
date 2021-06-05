" Dependency searcher for metadata "
import dataclasses
from functools import partial
from itertools import starmap
from typing import List, Optional, Sequence

from odbinfo.pure.datatype import (BasicCall, BasicFunction, CommandDriven,
                                   DatabaseDisplay, DataObject, Identifier,
                                   Metadata, Module, Query, TextDocument,
                                   Token, UseCase, get_identifier)


def search_dependencies(metadata: Metadata) -> List[UseCase]:
    " dependency search in `metadata`"

    return (search_callable_in_callable(metadata.callables()) +
            search_string_refs_in_callables(metadata.tables, metadata.callables()) +
            search_string_refs_in_callables(metadata.views, metadata.callables()) +
            search_string_refs_in_callables(metadata.queries, metadata.callables()) +
            search_string_refs_in_callables(metadata.reports, metadata.callables()) +
            rewrite_module_callable_links(metadata.modules()) +
            search_deps_in_queries(metadata.tables, metadata.queries) +
            search_deps_in_queries(metadata.views, metadata.queries) +
            search_deps_in_queries(metadata.queries, metadata.queries) +
            search_deps_in_queries(metadata.tables, metadata.views) +
            search_deps_in_queries(metadata.views, metadata.views) +
            search_deps_in_commanddriven(metadata.tables,
                                         metadata.reports) +
            search_deps_in_commanddriven(metadata.views, metadata.reports) +
            search_deps_in_commanddriven(metadata.queries, metadata.reports) +
            search_deps_in_commanddriven(metadata.tables,
                                         metadata.subforms()) +
            search_deps_in_commanddriven(metadata.views, metadata.subforms()) +
            search_deps_in_commanddriven(metadata.queries, metadata.subforms()) +
            search_deps_in_documents(metadata.tables, metadata.documents) +
            search_deps_in_documents(metadata.views, metadata.documents) +
            search_deps_in_documents(metadata.queries, metadata.documents)
            )

#
# BasicFunction in BasicFunction
#


def _copy_module_tokens(modules):
    def copy_tokens(module):
        def copy_token(token):
            new_token = dataclasses.replace(token)
            new_token.link = token.link.copy()
            return new_token
        module.tokens = list(map(copy_token, module.tokens))
    list(map(copy_tokens, modules))


def _rewrite_module_token_links(modules):
    " scan module tokens for links"
    # process module source tokens to support callable links at module level
    # e.g /Lib1.Mod1/#macro
    # By rewriting Identifier(type="BasicFunction" local_id="Lib1.Mod1.call")
    # to Identifier("Module", "Lib1.Mod1", bookmark="call")
    def rewrite_module(module: Module):

        def rewrite_token(token: Token):

            def rewrite_link(link: Identifier):
                if not link.object_type == "callables":
                    return
                lmacro, lmodule, llib = link.local_id.split('.')
                new_link = Identifier("modules", f"{lmodule}.{llib}")
                new_link.bookmark = lmacro
                token.link.clear()
                token.link.append(new_link)

            if len(token.link) > 0:
                # breakpoint()
                identifier = token.link[0]
                rewrite_link(identifier)

        list(map(rewrite_token, module.tokens))

    list(map(rewrite_module, modules))


def _link_name_tokens(module: Module):
    def _link_name(index: int, acallable: BasicFunction):
        link_token(module.tokens[index], acallable)
    list(starmap(_link_name, zip(module.name_indexes, module.callables)))


def rewrite_module_callable_links(modules: Sequence[Module]) -> List[UseCase]:
    """ links to callables are rewritten to links to callables in
        modules (using #bookmarks)"""
    _copy_module_tokens(modules)
    _rewrite_module_token_links(modules)
    list(map(_link_name_tokens, modules))
    return []


def search_callable_in_callable(callables: Sequence[BasicFunction],
                                ) -> List[UseCase]:
    """ dependency search amoung the basic callables and linking the
        parsed tokens to the targets
        the callable tokens are linked during search
        the module tokens links are rewritten afterwards """
    use_cases = find_callable_in_callable(callables)

    return use_cases


def find_callable_in_callable(callables: Sequence[BasicFunction]) -> List[UseCase]:
    " find calls from one to another "
    def search_in_one(caller: BasicFunction):
        # caller's module
        def filter_own_module(call: BasicFunction):
            return (call.module == caller.module and
                    call.library == caller.library)

        # callables in own library
        def filter_own_library(call: BasicFunction):
            return (not (call.module == caller.module) and
                    call.library == caller.library)

        # callables in other libraries
        def filter_other_library(call: BasicFunction):
            return not call.library == caller.library

        # the order is crucial as it represents scope in OOBasic
        candidates = (list(filter(filter_own_module, callables)) +
                      list(filter(filter_own_library, callables)) +
                      list(filter(filter_other_library, callables)))
        consider_caller = partial(consider, caller)
        return sum(map(consider_caller, candidates), [])

    return sum(map(search_in_one, callables), [])


def link_token(token: Token, referand: DataObject):
    "link `token` to `acallable`"
    token.link.append(get_identifier(referand))


def consider(caller: BasicFunction, candidate_callee: BasicFunction) -> List[UseCase]:
    " find calls in `caller` to `candidate_callee`"
    # print("Considering: ", caller.title, candidate_callee.title)

    def match_and_not_linked(acall: BasicCall):
        if acall.module_token:
            if acall.module_token.text.upper() != candidate_callee.module.upper():
                return False, acall

        return (acall.name_token.text.upper() == candidate_callee.name.upper()
                and len(acall.name_token.link) == 0, acall)

    def process_match(acall: BasicCall):
        link_token(acall.name_token, candidate_callee)
        return UseCase(
            get_identifier(caller),
            get_identifier(candidate_callee),
            "invokes")

    use_cases = []
    for match, ntoken in map(match_and_not_linked, caller.calls):
        if match:
            use_cases.append(process_match(ntoken))
    return use_cases

#
# Tables, Views, Queries, Reports in Callables
#


def search_string_refs_in_callables(dataobjects: Sequence[DataObject],
                                    callables: Sequence[BasicFunction]) -> List[UseCase]:
    """ search for references to table, views, queries or reports
        in callable string literals """
    def search_refs_in_one(acallable: BasicFunction) -> List[UseCase]:
        def ref_in_one(dataobject: DataObject) -> List[UseCase]:
            def compare_ref(string_token: Token) -> List[UseCase]:
                if dataobject.name == string_token.text[1:-1]:
                    link_token(string_token, dataobject)
                    return [UseCase(get_identifier(acallable),
                                    get_identifier(dataobject),
                                    "string refers")]
                return []
            return sum(map(compare_ref, acallable.strings), [])
        return sum(map(ref_in_one, dataobjects), [])

    return sum(map(search_refs_in_one, callables), [])


#
# dataobject in Queries
#


def search_deps_in_queries(dataobjects: Sequence[DataObject],
                           queries: Sequence[Query]) -> List[UseCase]:
    " find uses of dataobject in queries "
    def find_tables_in_query(query: Query) -> List[UseCase]:
        " find table uses in `query` "
        def find_table_in_query(table: DataObject) -> List[UseCase]:
            def find_table_in_token(token: Token) -> List[UseCase]:
                use_cases = []
                if token.text[1:-1] == table.name:
                    link_token(token, table)
                    use_cases.append(UseCase(get_identifier(query),
                                             get_identifier(table),
                                             "queries"))
                return use_cases

            return sum(map(find_table_in_token, query.table_tokens), [])
        return sum(map(find_table_in_query, dataobjects), [])

    return sum(map(find_tables_in_query, queries), [])

#
# DataObject (query, view, table) in Report
#


def search_deps_in_commanddriven(dataobjects: Sequence[DataObject],
                                 reports: Sequence[CommandDriven]) -> List[UseCase]:
    " find uses of dataobject in report"
    def find_deps_in_report(report: CommandDriven) -> List[UseCase]:
        " find dependency uses in `report` "
        def find_one_dep(dependency: DataObject) -> Optional[UseCase]:
            if report.command.text == dependency.name:
                dependency_id = get_identifier(dependency)
                report.command.link = dependency_id
                return UseCase(get_identifier(report),
                               dependency_id,
                               "queries")

            return None

        return [obj for obj in map(find_one_dep, dataobjects) if obj is not None]

    return sum(map(find_deps_in_report, reports), [])


def search_deps_in_documents(dataobjects: Sequence[DataObject],
                             documents: Sequence[TextDocument]) -> List[UseCase]:
    " find uses of dataobject in document"
    def find_deps_in_doc(document: TextDocument) -> List[UseCase]:
        " find dependency uses in `report` "
        def find_one_dep(dependency: DataObject) -> List[UseCase]:

            def find_in_databasedisplay(display: DatabaseDisplay) -> Optional[UseCase]:
                if display.table.text == dependency.name:
                    dependency_id = get_identifier(dependency)
                    display.table.link = dependency_id
                    return UseCase(get_identifier(document),
                                   dependency_id,
                                   "queries")

                return None
            return [obj for obj in map(find_in_databasedisplay, document.fields) if obj is not None]
        return sum(map(find_one_dep, dataobjects), [])
    return sum(map(find_deps_in_doc, documents), [])
