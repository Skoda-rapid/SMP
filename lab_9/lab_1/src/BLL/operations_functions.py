from math import sqrt

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль."
    return a / b

def find_sqrt(a):
    return sqrt(a)

def find_remainder(a, b):
    return a % b

def to_power(a, b):
    return a ** b