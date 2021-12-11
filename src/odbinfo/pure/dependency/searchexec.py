""" dependency search in basicfunctions """
from typing import Sequence

from odbinfo.pure.datatype import BasicFunction, Usable
#
# BasicFunction in BasicFunction
#
from odbinfo.pure.dependency.util import search_combinations


def remove_recursive_calls(funcs: Sequence[BasicFunction]):
    """remove the probably unintended recursive call made by assignment"\
        "of the return value"""
    for function in funcs:
        function.remove_recursive_calls()


def search_calls(source: BasicFunction, targets: Sequence[BasicFunction]):
    """ search for calls from source in `targets`"""

    # source's module
    def filter_own_module(call: BasicFunction):
        return (call.module == source.module
                and call.library == source.library)

    # targets in own library
    def filter_own_library(call: BasicFunction):
        return (not (call.module == source.module)
                and call.library == source.library)

    # targets in other libraries
    def filter_other_library(call: BasicFunction):
        return not call.library == source.library

    # the order is crucial as it represents scope in OOBasic
    ordered_targets = (list(filter(filter_own_module, targets))
                       + list(filter(filter_own_library, targets))
                       + list(filter(filter_other_library, targets)))
    for candidate in ordered_targets:
        source.consider_calls(candidate)


def search_callable_in_callable(callables: Sequence[BasicFunction]) -> None:
    """ dependency search amoung the basic targets and linking the
    parsed tokens to the targets
    the callable tokens are linked during search
    the module tokens links are rewritten afterwards
    find calls from one to another """

    for acallable in callables:
        search_calls(acallable, callables)
    remove_recursive_calls(callables)


#
# Tables, Views, Queries, Reports, TextDocument in BasicFunction
#
def search_string_refs_in_callables(dataobjects: Sequence[Usable],
                                    callables: Sequence[BasicFunction]) -> None:
    """ search for references to table, views, queries or reports
        in callable string literals """
    search_combinations(sources=callables, targets=dataobjects)
