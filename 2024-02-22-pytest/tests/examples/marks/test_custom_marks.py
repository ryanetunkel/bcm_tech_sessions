import pytest

from pytest_demo.examples.marks import custom_marks as module

URL = "https://httpstat.us/200"


@pytest.mark.integration
def test_internet_connection():
    """Make sure we get a 200 HTTP response"""
    result = module.internet_connection(URL)
    assert result == 200
