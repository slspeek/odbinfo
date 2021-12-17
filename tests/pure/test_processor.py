""" Tests for the processor """
from odbinfo.pure.datatype.ui import SubForm
from odbinfo.pure.processor import ModulePreprocessor, set_depth


def test_set_depth():
    """ test set_depth """
    root = SubForm("", "", "", "", "", "", "", "", [], [])
    child = SubForm("", "", "", "", "", "", "", "", [], [])
    root.subforms.append(child)
    set_depth(0, root)
    assert root.depth == 0
    assert child.depth == 1


def test_link_name_tokens(module_single_function):
    preprocessor = ModulePreprocessor()

    module_single_function.accept(preprocessor)

    func = module_single_function.callables[0]
    name_token = module_single_function.tokens[func.name_token_index]
    assert name_token.link == func.identifier
