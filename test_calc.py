# Module de unit test
from calculator import Calculator


def test_add():
    x, y, z, t = 10, 2, 7, 3
    instance = Calculator()
    assert instance.add(x, y, z, t) == x + y + z + t, "Add method has a problem"


def test_substract():
    x, y, z, t = 10, 2, 7, 3
    instance = Calculator()
    assert instance.substract(x, y, z, t) == x - y - z - t, "Substract method has a problem"


def test_multiply():
    x, y, z, t = 10, 2, 7, 3
    instance = Calculator()
    assert instance.multiply(x, y, z, t) == x * y * z * t, "Multiply method has a problem"


def test_divide():
    x, y, z, t = 10, 2, 0, 3
    instance = Calculator()
    assert instance.divide(x, y, z, t) == x / y / z / t, "Divide method has a problem"
