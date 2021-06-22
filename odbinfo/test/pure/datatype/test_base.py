" test base classes "
from odbinfo.pure.datatype import Table


def test_post_init():
    table = Table("Plant", "All plant attributes", [], [], [])
    assert not table.obj_id == 0
