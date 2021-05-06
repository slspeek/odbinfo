" Dependency searcher for metadata "
import operator
from functools import partial, reduce

from odbinfo.pure.datatype import (BasicCall, Callable, Metadata, Token,
                                   UseCase, get_identifier)


def search_dependencies(metadata: Metadata) -> [UseCase]:
    " dependency search in `metadata`"
    return search_callable_in_callable(metadata.callables())


def search_callable_in_callable(callables: [Callable]) -> [UseCase]:
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

    def make_use_case(acall: BasicCall):
        link_token(acall.name_token, candidate_callee)
        return UseCase(
            get_identifier(caller),
            get_identifier(candidate_callee),
            "invokes")

    use_cases = []
    for match, ntoken in map(match_and_not_linked, caller.calls):
        if match:
            use_cases.append(make_use_case(ntoken))
    return use_cases
