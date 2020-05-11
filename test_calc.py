# Module de unit test
from calculator import Calculator


def test_multiplyADD():
    x, y = 10, 2
    instance = Calculator()
    assert instance.add(x, y) == x * y, "Add method has a problem"


def test_substract():
    x, y = 10, 2
    instance = Calculator()
    assert instance.substract(x, y) == x - y, "Substract method has a problem"


def test_multiply():
    x, y = 10, 2
    instance = Calculator()
    assert instance.multiply(x, y) == x * y, "Multiply method has a problem"


def test_divide():
    x, y = 10, 2
    instance = Calculator()
    assert instance.divide(x, y) == x / y, "Divide method has a problem"
