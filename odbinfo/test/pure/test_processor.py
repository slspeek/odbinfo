" Tests for the processor "

from odbinfo.pure.datatype import SubForm
from odbinfo.pure.processor import height, set_depth


def test_set_depth():
    " test set_depth "
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    set_depth(0, root)
    assert root.depth == 0
    assert child.depth == 1


def test_height_one():
    " test height of subform tree "
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    assert height(root) == 1


def test_height_zero():
    " test height of subform tree "
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    assert height(root) == 0
