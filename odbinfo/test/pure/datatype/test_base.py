" test base classes "
import pytest

from odbinfo.pure.datatype import (EmbeddedQuery, Identifier, Report, Table,
                                   content_type, get_identifier)
from odbinfo.pure.datatype.base import NamedNode, Node, WebPage


def test_node_empty_children():
    " verifies that the default implementation of children returns"\
        " the empty iterator "
    node = Node()
    assert not node.children()


def test_node_all_objects():
    " a child occurs in all_objects "
    node = Node()
    child = Node()

    class ANode(Node):
        def children(self):
            return [child]

    node = ANode()
    assert child in node.all_objects()


def test_node_users_match():
    " default implementation of users_match does string equality "
    named = NamedNode("foo")
    assert named.users_match("foo")


@pytest.mark.parametrize("parent,parent_link",
                         [(None, None),
                          (WebPage("parent"),
                           get_identifier(WebPage("parent")))])
def test_webpage_set_parents_single_none(parent, parent_link):
    single = WebPage("index")
    single.set_parents(parent)
    assert single.parent_link == parent_link


def test_webpage_set_parents_with_children():
    child = WebPage("child")
    non_page = Node()

    class AWebPage(WebPage):

        def children(self):
            return [child, non_page]

    page = AWebPage("page")
    page.set_parents(None)
    assert page.parent_link is None
    assert child.parent_link == get_identifier(page)


def test_get_identifier():
    usable = EmbeddedQuery("QPlant", "SELECT * FROM Plant")
    usable.parent = Report("Report", "Plant", "table", "doc", [])
    assert get_identifier(usable) == Identifier(
        'report', 'Report', 'OBJID_NOT_SET')


def test_get_identifier_error():
    node_wo_parent = Node()

    with pytest.raises(RuntimeError):
        get_identifier(node_wo_parent)


def test_content_type():
    "test content_type"
    assert content_type(WebPage) == "webpage"
