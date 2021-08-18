" test base classes "
from odbinfo.pure.datatype import (EmbeddedQuery, Identifier, Report, Table,
                                   content_type, get_identifier)


def test_post_init():
    table = Table("Plant", "All plant attributes", [], [], [])
    assert not table.obj_id == 0


def test_get_identifier():
    usable = EmbeddedQuery("QPlant", "SELECT * FROM Plant")
    usable.parent = Report("Report", "Plant", "table", "doc", [])
    assert get_identifier(usable) == Identifier(
        'report', 'Report', 'OBJID_NOT_SET')


def test_content_type():
    "test content_type"
    assert content_type(Table) == "table"
