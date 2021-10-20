" dependency search in basicfunctions "
from functools import partial
from typing import Sequence

from odbinfo.pure.datatype import (BasicCall, BasicFunction, Identifier,
                                   Module, Token, WebPage, content_type)
from odbinfo.pure.dependency.util import link_token

#
# BasicFunction in BasicFunction
#


def _rewrite_module_token_links(modules):
    " scan module tokens for links"
    # process module source tokens to support callable links at module level
    # e.g /Lib1.Mod1/#macro
    # By rewriting Identifier(type="BasicFunction" local_id="call.Mod1.Lib1")
    # to Identifier("Module", "Mod1.Lib1", bookmark="call")

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


def remove_recursive_calls(funcs: Sequence[BasicFunction]):
    "remove the probably unintended recursive call made by assignment"\
        "of the return value"
    for function in funcs:
        for call in function.calls:
            if call.name_token.text.lower() == function.name.lower():
                call.name_token.link = None


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
    remove_recursive_calls(callables)


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


def search_string_refs_in_callables(dataobjects: Sequence[WebPage],
                                    callables: Sequence[BasicFunction]) -> None:
    """ search for references to table, views, queries or reports
        in callable string literals """
    def search_refs_in_one(acallable: BasicFunction) -> None:
        def ref_in_one(dataobject: WebPage) -> None:
            def compare_ref(string_token: Token) -> None:
                if dataobject.users_match(string_token.text[1:-1]):
                    link_token(string_token, dataobject)
            for stoken in acallable.strings:
                compare_ref(stoken)
        for obj in dataobjects:
            ref_in_one(obj)
    for acallable in callables:
        search_refs_in_one(acallable)
