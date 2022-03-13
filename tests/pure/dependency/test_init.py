""" test search_dependencies """

from odbinfo.pure.dependency import search_dependencies


def test_search_dependencies(metadata_listbox):
    search_dependencies(metadata_listbox)
    assert len(list(metadata_listbox.actual_users)) == 1
