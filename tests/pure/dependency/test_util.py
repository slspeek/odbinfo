""" test the dependency search utilities """

from odbinfo.pure.datatype import Identifier, Table, Token
from odbinfo.pure.dependency import link_user_to_usuable


def test_link_token():
    """ test link_token when link already set """
    token = Token("'Plant'", 0, 0, False)
    link = Identifier("report", "Plant", None)
    token.link = link
    table = Table("Plant", "", [], [], [])
    link_user_to_usuable(token, table)
    assert token.link == table.identifier
