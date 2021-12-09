""" test the dependency search utilities """

from odbinfo.pure.datatype import Identifier, Table, Token


def test_link_to():
    """ test link_token when link already set """
    token = Token("'Plant'", 0, 0, False)
    link = Identifier("report", "Plant", None)
    token.link = link
    table = Table("Plant", "", [], [], [])
    token.link_to(table)
    assert token.link == table.identifier
