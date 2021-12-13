""" test the dependency search utilities """

from odbinfo.pure.datatype.base import BasicToken, Identifier
from odbinfo.pure.datatype.tabular import Table


def test_link_to():
    """ test link_token when link already set """
    token = BasicToken("'Plant'", 0, 0, False)
    link = Identifier("report", "Plant", None)
    token.link = link
    table = Table("Plant", "", [], [], [])
    token.link_to(table)
    assert token.link == table.identifier
