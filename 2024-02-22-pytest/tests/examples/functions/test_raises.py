# Test using the `pytest.raises` function
import pytest

from pytest_demo.examples.functions import raises as module


def test_check_if_more_than_42():
    """With an already existing exception"""
    number = 45
    with pytest.raises(ValueError):
        module.check_if_more_than_42(number)


def test_check_if_its_exactly_100():
    """With a custom exception"""
    with pytest.raises(module.CannotBeExactly100) as exc_info:
        module.check_if_its_exactly_100(100)
    # You can then inexpec the details of the exception

    # Check that the exception raised isthe one you expected
    # Lines 17-18 does this already
    assert exc_info.type is module.CannotBeExactly100
    # Check that the arguments you return in the exception is what you expect
    assert exc_info.value.msg == "Number cannot be exactly 100."
