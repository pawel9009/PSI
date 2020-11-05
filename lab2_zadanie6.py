import math


class Calculator:
    def add(x, y):
        return x+y

    def difference(x, y):
        return x-y

    def multiply(x, y):
        return x*y

    def divide(x, y):
        if y != 0:
            return x/y


class Sciencecalculator(Calculator):
    def pow(x, y):
        return x**y

    def sqrt(x):
        return math.sqrt(x)