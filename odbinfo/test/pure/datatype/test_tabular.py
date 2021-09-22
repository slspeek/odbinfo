" test the tabular datatypes "

from odbinfo.pure.datatype.tabular import Table


def test_post_init():
    table = Table("Plant", "All plant attributes", [], [], [])
    assert not table.obj_id == 0
