# Module de unit test
from calculator import Calculator


def test_multiply():
    x, y = 10, 2
    instance = Calculator()
    assert instance.multiply(x, y) == x * y, "Multiply method has a problem"
