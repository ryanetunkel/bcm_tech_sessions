# Bonus for capsys

from pytest_demo.examples.fixtures import caplog as module


def test_say_hello_if_name_not_str(caplog):
    """Test that we get the logger error if name is not string"""
    name = 123
    module.say_hello(name)
    assert "`name` is not a string, not saying hello" in caplog.text


def test_say_hello_if_name_str(capsys):
    """Test that we get printed output if name is str"""
    name = "User"
    module.say_hello(name)
    captured = capsys.readouterr()
    assert "Hello, User" in captured.out


def test_say_hello(caplog, capsys):
    """Test that we get the logger error if name is not string but no output in
    stdout"""
    name = 123
    module.say_hello(name)
    assert "`name` is not a string, not saying hello" in caplog.text
    captured = capsys.readouterr()
    assert "Hello, 123" not in captured.out
