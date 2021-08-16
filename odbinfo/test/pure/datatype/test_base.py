" test base classes "
from odbinfo.pure.datatype import (EmbeddedQuery, Identifier, Report, Table,
                                   get_identifier)


def test_post_init():
    table = Table("Plant", "All plant attributes", [], [], [])
    assert not table.obj_id == 0


def test_get_identifier():
    usable = EmbeddedQuery("QPlant", "SELECT * FROM Plant")
    usable.parent = Report("Report", "Plant", "table", "doc", [])
    assert get_identifier(usable) == Identifier(
        'report', 'Report', 'OBJID_NOT_SET')
