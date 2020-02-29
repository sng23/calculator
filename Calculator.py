import math


def fn_addition(a, b):
    return a + b


def fn_subtraction(a, b):
    return a - b


def fn_multiplication(a, b):
    return a * b


def fn_division(a, b):
    return a / b


def fn_square(a):
    return a * a


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = fn_addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = fn_subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = fn_multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = fn_division(a, b)
        return self.result

    def square(self, a):
        self.result = fn_square(a)
        return self.result

        return self.result
