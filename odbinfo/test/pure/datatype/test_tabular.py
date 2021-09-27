" test the tabular datatypes "

from odbinfo.pure.datatype import Column, Key, Query, QueryColumn
from odbinfo.pure.datatype.tabular import Table


def test_query_column():
    " test __post_init__"
    qcolumn = QueryColumn("id",  True, 2, "plants", "int", "", "",
                          1, True, True, True)
    assert qcolumn.nullable == "Nullable_Unknown"


def test_query():
    " test __post_init__"
    query = Query("plants", "select * from plants")
    assert query.command == "SELECT *\nFROM   plants"


def test_column():
    " test __post_init__"
    column = Column("id", True, 2, "Plant", 2, "", "", "", "")
    assert column.nullable == "Nullable_Unknown"


def test_key():
    " test __post_init__"
    key = Key("PK_91", [], [], "plants", 1, 1, 1)
    assert key.typename == "Primary"
    assert key.update_rule == "Restrict"
    assert key.delete_rule == "Restrict"


def test_table_post_init():
    table = Table("Plant", "All plant attributes", [], [], [])
    assert not table.obj_id == 0


def test_embeddedquery_children():
    equery = Query("emdedded", 'select * from  Plant')
    assert list(equery.children()) == []
