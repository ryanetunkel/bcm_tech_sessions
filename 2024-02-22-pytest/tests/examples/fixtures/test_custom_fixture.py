import pytest
from pytest_demo.examples.fixtures import custom_fixture as module


@pytest.fixture(name="names", scope="function")
def fixture_names():
    return ["John", "Jane", "Mary"]


def test_check_if_john_in_group_false(names):
    # Replace John with Mark
    names[0] = "Mark"
    assert not module.check_if_john_in_group(names)


def test_check_if_john_in_group_true(names):
    # Should pass even though we changed John to Mark in the last one
    assert module.check_if_john_in_group(names)
