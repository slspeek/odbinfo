""" Tests for the processor """
from odbinfo.pure import processor
from odbinfo.pure.datatype.base import Identifier, UseLink
from odbinfo.pure.datatype.ui import SubForm


def test_set_depth():
    """ test set_depth """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    processor.FormPreprocessor().set_depth(0, root)
    assert root.depth == 0
    assert child.depth == 1


def test_height_one():
    """ test height of subform tree """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    assert processor.FormPreprocessor().height(root) == 1


def test_height_zero():
    """ test height of subform tree """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    assert processor.FormPreprocessor().height(root) == 0


def test_link_name_tokens(module_single_function):
    preprocessor = processor.ModulePreprocessor()

    module_single_function.accept(preprocessor)

    func = module_single_function.callables[0]
    name_token = module_single_function.tokens[func.name_token_index]
    assert name_token.link == func.identifier


def test_undouble_used_by():
    assert processor.merge_used_by([Identifier("foo", "bar", "67"),
                                    Identifier("foo", "bar", "1")]) == \
        [Identifier("foo", "bar", "67,1")]


def test_undouble_used_by_three():
    assert processor.merge_used_by([Identifier("foo", "bar", "67"),
                                    Identifier("foo", "bar", "1"),
                                    Identifier("foo", "bar", "42"),
                                    Identifier("goof", "fox", "13"),
                                    ]) == \
        [Identifier("foo", "bar", "67,1,42"),
            Identifier("goof", "fox", "13"),
         ]


def test_undouble_uses():
    assert processor.undouble_uses(
        [UseLink(Identifier("foo", "bar", "67"), ["45"]),
         UseLink(Identifier("foo", "bar", "67"), ["23"]),
         ]) == \
        [UseLink(Identifier("foo", "bar", "67"), ["45", "23"])]


def test_undouble_uses_three():
    assert processor.undouble_uses(
        [UseLink(Identifier("foo", "bar", "67"), ["45"]),
         UseLink(Identifier("foo", "bar", "67"), ["23"]),
         UseLink(Identifier("bar", "bar", None), ["16"]),
         ]) == \
        [UseLink(Identifier("foo", "bar", "67"), ["45", "23"]),
            UseLink(Identifier("bar", "bar", None), ["16"]),
         ]
