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
    l = [10, 2, 0, 3]
    instance = Calculator()
    assert instance.divide(l) == l[0] / l[1] / l[3], "Divide method has a problem"


test_add()
test_substract()
test_multiply()
test_divide()
