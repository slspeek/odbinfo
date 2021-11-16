"test for config module"

import pytest

from odbinfo.pure.datatype.config import ConfigurationAttributeNotSet


def test_exception():
    with pytest.raises(ConfigurationAttributeNotSet) as exception:
        raise ConfigurationAttributeNotSet("foo")
    assert exception.match("Configuration attribute foo was not set")
