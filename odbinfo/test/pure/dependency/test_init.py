" test search_dependencies "

from odbinfo.pure.dependency import search_dependencies
from odbinfo.test.pure.datatype import factory


def test_search_dependencies():
    meta = factory.metadata_listbox()
    search_dependencies(meta)
    assert len(list(meta.all_active_users())) == 1
