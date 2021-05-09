" Dependency searcher for metadata "
import dataclasses
import operator
from functools import partial, reduce

from odbinfo.pure.datatype import (BasicCall, Callable, Identifier, Metadata,
                                   Module, Token, UseCase, get_identifier)


def search_dependencies(metadata: Metadata) -> [UseCase]:
    " dependency search in `metadata`"
    return search_callable_in_callable(metadata.callables(), metadata.modules())


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
    # By rewriting Identifier(type="Callable" local_id="Lib1.Mod1.call")
    # to Identifier("Module", "Lib1.Mod1", bookmark="call")
    def rewrite_module(module: Module):

        def rewrite_token(token: Token):

            def rewrite_link(link: Identifier):
                llib, lmodule, lmacro = link.local_id.split('.')
                new_link = Identifier("modules", f"{llib}.{lmodule}")
                new_link.bookmark = lmacro
                token.link.clear()
                token.link.append(new_link)

            if len(token.link) > 0:
                # breakpoint()
                identifier = token.link[0]
                rewrite_link(identifier)

        list(map(rewrite_token, module.tokens))

    list(map(rewrite_module, modules))


def search_callable_in_callable(callables: [Callable],
                                modules: [Module]) -> [UseCase]:
    """ dependency search amoung the basic callables and linking the
        parsed tokens to the targets
        the callable tokens are linked during search
        the module tokens links are rewritten afterwards """
    use_cases = find_callable_in_callable(callables)
    _copy_module_tokens(modules)
    _rewrite_module_token_links(modules)

    return use_cases


def find_callable_in_callable(callables: [Callable]) -> [UseCase]:
    " find calls from one to another "
    def search_in_one(caller: Callable):
        # caller's module
        def filter_own_module(call: Callable):
            return (call.module == caller.module and
                    call.library == caller.library)

        # callables in own library
        def filter_own_library(call: Callable):
            return (not (call.module == caller.module) and
                    call.library == caller.library)

        # callables in other libraries
        def filter_other_library(call: Callable):
            return not call.library == caller.library

        # the order is crucial as it represents scope in OOBasic
        candidates = (list(filter(filter_own_module, callables)) +
                      list(filter(filter_own_library, callables)) +
                      list(filter(filter_other_library, callables)))
        consider_caller = partial(consider, caller)
        return reduce(operator.add,
                      map(consider_caller, candidates), [])

    return reduce(operator.add, map(search_in_one, callables), [])


def link_token(token: Token, acallable: Callable):
    "link `token` to `acallable`"
    token.link.append(get_identifier(acallable))


def consider(caller: Callable, candidate_callee: Callable) -> [UseCase]:
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
