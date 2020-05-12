
# class calculator
# Test project for Travis CI
from functools import reduce
from operator import truediv

class Calculator():

    # Multiplication
    def multiply(self, *p_val: float) -> float:
        return reduce((lambda x, y: x * y), p_val)

    # substraction
    def substract(self, *p_val: float) -> float:
        return reduce((lambda x, y: x - y), p_val)

    # addition
    def add(self, *p_val: float) -> float:
        return reduce((lambda x, y: x + y), p_val)

    # division
    def divide(self, p_val: list) -> float:
        return reduce((lambda x, y: x / y if y != 0 else x), p_val)
