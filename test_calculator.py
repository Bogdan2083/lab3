import pytest
from calculator import add, reverse_string

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("GitHub") == "buHtiG"  # замінили buhiG на buHtiG

def test_reverse_string_exception():
    with pytest.raises(TypeError):
        reverse_string(123)