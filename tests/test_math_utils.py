from src.math_utils import add

def test_add_positive():
    assert add(3, 5) == 8

def test_add_negative():
    assert add(-2, -4) == -6

