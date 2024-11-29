import os
import sys

# Отримуємо абсолютний шлях до кореневої директорії проєкту
lab1_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, lab1_root)

from shared.constants.global_variables import Button
from .operations_functions import *  # Необхідно уточнити, які саме функції імпортуються


def calc_result(num1, oper, num2=0):
    """
    Функція для виконання математичних операцій над двома числами.

    Параметри:
        num1 (str or float): Перше число, з яким буде проводитись операція.
        oper (str): Оператор, який визначає, яку операцію виконати.
        num2 (str or float, optional): Друге число, необхідне для бінарних операцій. За замовчуванням 0.

    Повертає:
        float or str: Результат виконаної операції або повідомлення про помилку, якщо оператор некоректний.
    """
    a = float(num1)
    b = float(num2)

    # Словник з операціями
    operations = {
        Button.ADDITION.value: add,
        Button.SUBTRACTION.value: subtract,
        Button.MULTIPLICATION.value: multiply,
        Button.DIVISION.value: divide,
        Button.SQRT.value: find_sqrt,
        Button.REMAINDER.value: find_remainder,
        Button.POWER.value: to_power,
    }

    # Виконання операції відповідно до переданого оператора
    if oper in operations:
        if oper == Button.SQRT.value:
            return operations[oper](a)
        else:
            return operations[oper](a, b)
    else:
        return "Неправильний оператор"
