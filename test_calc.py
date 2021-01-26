# Module de unit test
from calculator import Calculator


def test_add():
    print("Execution of test for add() function")
    x, y, z, t = 10, 2, 7, 3
    instance = Calculator()
    assert instance.add(x, y, z, t) == x + y + z + t, "Add method has a problem"
    print("Execution of test for add() function => OK")


def test_substract():
    print("Execution of test for substract() function")
    x, y, z, t = 10, 2, 7, 3
    instance = Calculator()
    assert instance.substract(x, y, z, t) == x - y - z - t, "Substract method has a problem"
    print("Execution of test for substract() function => OK")


def test_multiply():
    print("Execution of test for multiply() function")
    x, y, z, t = 10, 2, 7, 3
    instance = Calculator()
    assert instance.multiply(x, y, z, t) == x * y * z * t, "Multiply method has a problem"
    print("Execution of test for multiply() function => OK")


def test_divide():
    print("Execution of test for diveide() function")
    l = [10, 2, 0, 3]
    instance = Calculator()
    assert instance.divide(l) == l[0] / l[1] / l[3], "Divide method has a problem"
    print("Execution of test for diveide() function => OK")


def test_concat():
    print("Execution of test for concatenate() function")
    l = [10, 2, 0, 3]
    l = [str(i) for i in l]
    instance = Calculator()
    assert instance.concat(l) == "10203", "Concat method has a problem"
    print("Execution of test for concatenate() function=> OK")


test_add()
test_substract()
test_multiply()
test_divide()
test_concat()
