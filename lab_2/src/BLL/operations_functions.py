from math import sqrt


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Помилка: ділення на нуль неможливе.")


def find_sqrt(a):
    return sqrt(a)


def find_remainder(a, b):
    return a % b


def to_power(a, b):
    return a**b
