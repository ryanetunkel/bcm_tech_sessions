# Test using pytest function `deprecated_call`

import pytest

from pytest_demo.examples.functions import deprecated_call

##########
## Test ##
##########


def test_api_v1_check_if_john_in_names_deprecated_call_raised():
    """Test that a `DeprecationWarning` is raised"""
    names = ["john", "Mary"]
    with pytest.deprecated_call():
        result = deprecated_call.api_v1_check_if_john_in_names(names)
    assert result
