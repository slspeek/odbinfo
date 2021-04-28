" Dependency searcher for metadata "
from functools import partial

from odbinfo.pure.datatype import (Callable, Metadata, Token, UseCase,
                                   get_identifier)
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer


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


def corresponding_token(token_list: [Token], token: Token) -> Token:
    " find `token` by index in `token_list` "
    for atoken in token_list:
        if atoken.index == token.index:
            return atoken
    raise ValueError(f"Token: {token} not found in {token_list}")


# def isprepanded_by_dot_id(token_list: [Token], token: Token, module: str):
#     " See if IDENTIFIER token is preseeded by module. "
#     index = token.index
#     if index > 0:
#         index -= 1
#         if token_list[index].type == OOBasicLexer.DOT:
#             if index > 0:
#                 index -= 1
#
#                 if token_list[index].type == OOBasicLexer.IDENTIFIER:
#                     if token_list[index].text == module:
#                         return True
#     return False


def consider(caller: Callable, candidate_callee: Callable) -> [UseCase]:
    " find calls in `caller` to `candidate_callee`"
    # print("Considering: ", caller.title, candidate_callee.title)
    calls = []
    identifiers = list(filter(lambda tok: tok.type == OOBasicLexer.IDENTIFIER,
                              caller.body_tokens))
    for token in identifiers:
        if token.text.upper() == candidate_callee.name.upper():
            callee_link = get_identifier(candidate_callee)

            corres_token = corresponding_token(caller.tokens, token)
            # if isprepanded_by_dot_id(caller.tokens, corres_token,
            #                          candidate_callee.module):
            #     pass
            # See if not linked yet
            if len(corres_token.link) == 0:
                calls.append(UseCase(
                    get_identifier(caller),
                    callee_link,
                    "invokes")
                )
                corres_token.link.append(callee_link)
    return calls
