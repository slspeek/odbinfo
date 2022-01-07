""" Tests for the processor """
from odbinfo.pure.datatype.base import Identifier
from odbinfo.pure.datatype.ui import SubForm
from odbinfo.pure.processor import (FormPreprocessor, ModulePreprocessor,
                                    undouble_used_by)


def test_set_depth():
    """ test set_depth """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    FormPreprocessor().set_depth(0, root)
    assert root.depth == 0
    assert child.depth == 1


def test_height_one():
    """ test height of subform tree """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    assert FormPreprocessor().height(root) == 1


def test_height_zero():
    """ test height of subform tree """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    assert FormPreprocessor().height(root) == 0


def test_link_name_tokens(module_single_function):
    preprocessor = ModulePreprocessor()

    module_single_function.accept(preprocessor)

    func = module_single_function.callables[0]
    name_token = module_single_function.tokens[func.name_token_index]
    assert name_token.link == func.identifier


def test_undouble_used_by():
    assert undouble_used_by([Identifier("foo", "bar", "67"),
                             Identifier("foo", "bar", "1")]) == \
        [Identifier("foo", "bar", None)]
