""" test base classes """
import re

import pytest

from odbinfo.pure.datatype import (EmbeddedQuery, Identifier, Report,
                                   content_type)
from odbinfo.pure.datatype.base import (Node, NoWebPageAncestorException,
                                        WebPage, get_identifier, hugo_filename)


def test_hugo_filename_to_lower():
    assert hugo_filename("Foo") == "foo"


def test__hugo_filename_spaces():
    assert hugo_filename("F oo") == "f-oo"


def test_href_webpage(table_plant):
    assert table_plant.href == \
        "../table/plant/index.html"


def test_href_control(form):
    subform = form.subforms[0]
    subform.parent = form
    subform.obj_id = "42"
    assert subform.href == \
        "../form/myform/index.html#42"


def test_to_dict_identitifier_no_bookmark():
    identifier = Identifier("foo", "bar", None)
    assert identifier.to_dict() == {'content_type': "foo", 'local_id': "bar"}


def test_to_dict_identitifier():
    identifier = Identifier("foo", "bar", "barbar")
    assert identifier.to_dict() == {'content_type': "foo",
                                    'local_id': "bar",
                                    "bookmark": "barbar"}


def test_node_to_dict(table_plant, foreignkey_family):
    assert table_plant.to_dict()["keys"][0] == foreignkey_family.to_dict()


def test_node_empty_children():
    """ verifies that the default implementation of children returns"\
        " the empty iterator """
    node = Node()
    assert not node.children()


def test_node_all_objects():
    """ a child occurs in all_objects """
    child = Node()

    class ANode(Node):
        def children(self):
            return [child]

    node = ANode()
    assert child in node.all_objects()


def test_node_users_match(table_plant):
    """ default implementation of users_match does string equality """
    assert table_plant.users_match("plant")


@pytest.mark.parametrize("parent,parent_link",
                         [(None, None),
                          (WebPage("parent"),
                           get_identifier(WebPage("parent")))])
def test_webpage_set_parents_single_none(parent, parent_link):
    single = WebPage("index")
    single.set_parent_links(parent)
    assert single.parent_link == parent_link


def test_webpage_set_parents_with_children():
    child = WebPage("child")
    non_page = Node()

    class AWebPage(WebPage):

        def children(self):
            return [child, non_page]

    page = AWebPage("page")
    page.set_parent_links(None)
    assert page.parent_link is None
    assert child.parent_link == get_identifier(page)


def test_get_identifier():
    usable = EmbeddedQuery("QPlant", "SELECT * FROM Plant")
    usable.parent = Report("Report", "Plant", "table", "doc", [])
    assert get_identifier(usable) == Identifier(
        'report', 'Report', 'OBJID_NOT_SET')


def test_get_identifier_error():
    node_wo_parent = Node()

    with pytest.raises(NoWebPageAncestorException) as exception:
        get_identifier(node_wo_parent)
    assert exception.match(
        re.escape("No WebPage ancestor for Node(obj_id='OBJID_NOT_SET')"))


def test_content_type():
    """test content_type"""
    assert content_type(WebPage) == "webpage"
