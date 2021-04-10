" tests for datatype "
from odbinfo.pure.datatype import Column, Key, PythonModule, Query, QueryColumn


def test_python_module():
    " test __post_init__"
    pmodule = PythonModule("Standard", "Module1", "")
    assert pmodule.title == "Standard.Module1"


def test_query_column():
    " test __post_init__"
    qcolumn = QueryColumn("id", True, 2, "plants", "int", "", "",
                          True, True, True)
    assert qcolumn.nullable == "Nullable_Unknown"


def test_query():
    " test __post_init__"
    query = Query("plants", "select * from plants", [])
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
