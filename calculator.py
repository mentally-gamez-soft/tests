
# class calculator
# Test project for Travis CI
from functools import reduce

class Calculator():

    # Multiplication
    def multiply(self, *p_val: int) -> int:
        return reduce((lambda x, y: x * y), p_val)

    # substraction
    def substract(self, *p_val: int) -> int:
        return reduce((lambda x, y: x - y), p_val)

    # addition
    def add(self, *p_val: int) -> int:
        return reduce((lambda x, y: x + y), p_val)

    # division
    def divide(self, *p_val: int) -> int:
        return reduce((lambda x, y: x / y), p_val)
