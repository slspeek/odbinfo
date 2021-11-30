""" test dependency search in ui """

from odbinfo.pure.datatype.base import WebPage
from odbinfo.pure.dependency.searchui import (
    search_basicfunction_in_eventlistener, search_deps_in_commander,
    search_deps_in_documents)


def test_search_deps_in_commander_match(table_plant, report):
    """match"""
    search_deps_in_commander([table_plant], [report])
    assert report.link == table_plant.identifier


def test_search_deps_in_commander_no_match(table_plant, report_embeddedquery):
    """no match"""
    search_deps_in_commander(
        [table_plant], [report_embeddedquery])
    assert not report_embeddedquery.link


def test_search_deps_in_document_match(table_plant, textdoc):
    """match"""
    search_deps_in_documents([table_plant], [textdoc])
    assert textdoc.fields[0].link == table_plant.identifier


def test_search_deps_in_document_no_match(textdoc):
    """no match"""
    search_deps_in_documents([WebPage("not_plant")], [textdoc])
    assert not textdoc.fields[0].link


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
