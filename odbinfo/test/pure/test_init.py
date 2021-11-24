""" test installation verification """
import pytest

from odbinfo.pure.init import verify_installation


@pytest.mark.slow
def test_verify_installation():
    """ run verify_installation """
    verify_installation()
