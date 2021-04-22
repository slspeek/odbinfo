" Dependency searcher for metadata "
from odbinfo.pure.datatype import Callable, Metadata, UseCase, get_identifier
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer


def search_dependencies(metadata: Metadata) -> [UseCase]:
    " dependency search in `metadata`"
    return search_callable_in_callable(metadata.callables())


def search_callable_in_callable(callables: [Callable]) -> [UseCase]:
    " find calls from one to another "
    calls = []
    for caller in callables:
        for candidate_callee in callables:
            if candidate_callee == caller:
                continue
            calls.extend(consider(caller, candidate_callee))
    return calls


def consider(caller: Callable, candidate_callee: Callable) -> [UseCase]:
    " find calls in `caller` to `candidate_callee`"
    calls = []

    def search_target():
        " this could be more precise like 'Standard.Module.Routine' "
        return candidate_callee.name

    callee_id = search_target()
    for token in filter(lambda tok: tok.type == OOBasicLexer.IDENTIFIER,
                        caller.body_tokens):
        if token.text == callee_id:
            callee_link = get_identifier(candidate_callee)
            calls.append(UseCase(
                get_identifier(caller),
                callee_link,
                "invokes")
            )
            caller.tokens[caller.tokens.index(token)].link.append(callee_link)
    return calls
