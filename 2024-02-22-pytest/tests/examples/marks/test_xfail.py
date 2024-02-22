import pytest

from pytest_demo.examples.functions import warns as module


def test_check_if_fruit_passing():
    """The happy case test"""
    result = module.check_if_fruit("banana")
    assert result == True


def test_check_if_fruit_tomato():
    """See if warning is raised"""
    with pytest.warns(module.ThisFruitIsAlsoAVeggie):
        module.check_if_fruit("tomato")


# New below
@pytest.mark.xfail(reason="Will fail until Issue #123 is fixed")
def test_check_if_fruit_tomato_uppercase():
    """Passes tomato uppercase and should still return warning"""
    with pytest.warns(module.ThisFruitIsAlsoAVeggie):
        module.check_if_fruit("TOMATO")
    # With the existing code, this will never pass and should fail
    # until the code is fixed.
