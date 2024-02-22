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
