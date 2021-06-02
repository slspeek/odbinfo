" Tests for the processor "

from odbinfo.pure.datatype import SubForm
from odbinfo.pure.processor import set_depth


def test_set_depth():
    " test set_depth "
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    set_depth(0, root)
    assert root.depth == 0
    assert child.depth == 1
