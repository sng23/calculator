import math


def fn_addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = fn_addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
