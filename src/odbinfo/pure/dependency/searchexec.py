""" dependency search in basicfunctions """
from typing import Sequence

from odbinfo.pure.datatype import BasicCall, BasicFunction, Token, Usable

#
# BasicFunction in BasicFunction
#


def remove_recursive_calls(funcs: Sequence[BasicFunction]):
    """remove the probably unintended recursive call made by assignment"\
        "of the return value"""
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
        for candidate in candidates:
            consider(caller, candidate)
    for acallable in callables:
        search_in_one(acallable)
    remove_recursive_calls(callables)


def consider(caller: BasicFunction, candidate_callee: BasicFunction) -> None:
    """ find calls in `caller` to `candidate_callee`"""

    def match_and_not_linked(acall: BasicCall):
        if acall.module_token:
            if acall.module_token.text.upper() != candidate_callee.module.upper():
                return False, acall

        return (acall.name_token.text.upper() == candidate_callee.name.upper()
                and acall.name_token.link is None, acall)

    for match, fn_call in map(match_and_not_linked, caller.calls):
        if match:
            fn_call.name_token.link_to(candidate_callee)


#
# Tables, Views, Queries, Reports, TextDocument in BasicFunction
#


def search_string_refs_in_callables(dataobjects: Sequence[Usable],
                                    callables: Sequence[BasicFunction]) -> None:
    """ search for references to table, views, queries or reports
        in callable string literals """
    def search_refs_in_one(acallable: BasicFunction) -> None:
        def ref_in_one(dataobject: Usable) -> None:
            def compare_ref(string_token: Token) -> None:
                if dataobject.users_match(string_token.text[1:-1]):
                    string_token.link_to(dataobject)
            for stoken in acallable.strings:
                compare_ref(stoken)
        for obj in dataobjects:
            ref_in_one(obj)
    for acallable in callables:
        search_refs_in_one(acallable)
