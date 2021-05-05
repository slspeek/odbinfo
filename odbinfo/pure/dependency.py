" Dependency searcher for metadata "
from functools import partial

from odbinfo.pure.datatype import (Callable, Metadata, Token, UseCase,
                                   get_identifier)


def search_dependencies(metadata: Metadata) -> [UseCase]:
    " dependency search in `metadata`"
    return search_callable_in_callable(metadata.callables())


def search_callable_in_callable(callables: [Callable]) -> [UseCase]:
    " find calls from one to another "
    calls = []
    for caller in callables:
        lib = caller.library
        module = caller.module

        # callables in own module first
        def filter_own_module(lib: str, mod: str, call: Callable):
            return call.module == mod and call.library == lib

        candidates = filter(partial(filter_own_module, lib, module), callables)
        for candidate in candidates:
            if candidate == caller:
                continue
            calls.extend(consider(caller, candidate))

        # callables in own library
        def filter_own_library(lib: str, mod: str, call: Callable):
            return not (call.module == mod) and call.library == lib

        candidates = filter(
            partial(filter_own_library, lib, module), callables)
        for candidate in candidates:
            calls.extend(consider(caller, candidate))

        # callables in other libraries
        def filter_other_library(lib: str, call: Callable):
            return not call.library == lib

        candidates = filter(partial(filter_other_library, lib), callables)
        for candidate_callee in candidates:
            calls.extend(consider(caller, candidate_callee))
    return calls


def link_token(token: Token, acallable: Callable):
    "link `token` to `acallable`"
    token.link.append(get_identifier(acallable))


def consider(caller: Callable, candidate_callee: Callable) -> [UseCase]:
    " find calls in `caller` to `candidate_callee`"
    # print("Considering: ", caller.title, candidate_callee.title)

    def match_and_not_linked(acall):
        if len(acall) == 2:  # qualified call
            mod_token, name_token = acall
            module_name = mod_token.text

            if module_name.upper() != candidate_callee.module.upper():
                return False, name_token
        else:
            name_token = acall[0]
        return (name_token.text.upper() == candidate_callee.name.upper()
                and len(name_token.link) == 0, name_token)

    def make_use_case(name_token):
        link_token(name_token, candidate_callee)
        return UseCase(
            get_identifier(caller),
            get_identifier(candidate_callee),
            "invokes")

    use_cases = []
    for match, ntoken in map(match_and_not_linked, caller.calls):
        if match:
            use_cases.append(make_use_case(ntoken))
    return use_cases
