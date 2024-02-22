import sys

import pytest

from pytest_demo.examples.marks import skip as module


@pytest.mark.skip("this method doesn't exist yet")
def test_special_message_for_windows():
    """Test that a message is returned for Windows machines only"""
    result = module.special_message_for_windows()
    assert result == "Hello Windows!"


@pytest.mark.skipif(sys.version_info < (3, 11), reason="requires python3.11 or higher")
def test_exp2_python311_or_later():
    """Test the exp2 works as expected if python version is 3.11 or later"""
    result = module.exp2(4)
    assert result == 16

@pytest.mark.skipif(sys.version_info >= (3, 11), reason="requires python3.10 or lower")
def test_exp2_python310_or_earlier():
    """Test the exp2 works as expected if python version is 3.11 or later"""
    result = module.exp2(4)
    assert result == 16
