""" test dependency search in ui """

from odbinfo.pure.dependency.searchui import (
    search_basicfunction_in_eventlistener,
    )


def test_search_basicfunction_in_eventlistener(basic_function_main, eventlistener):
    """match"""
    search_basicfunction_in_eventlistener(
        [basic_function_main], [eventlistener])
    assert eventlistener.link == basic_function_main.identifier


def test_search_basicfunction_in_eventlistener_no_match(basic_function_notmain, eventlistener):
    """no match"""
    search_basicfunction_in_eventlistener(
        [basic_function_notmain], [eventlistener])
    assert not eventlistener.link
