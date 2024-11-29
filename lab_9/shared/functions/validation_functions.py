from shared.constants.global_variables import Button, Color
from shared.functions.ui_functions.handle_input import write_to_output
from shared.logger import Logger


def check_number(param):
    try:
        num = float(param)
        Logger.log(f"Перевірка числа: {param} — успішна")
        return num
    except ValueError:
        Logger.log(f"Помилка перевірки числа: {param} — це не число")
        write_to_output(f"'{param}' не є числом. Введіть число.")
        return check_number(input("Введіть число: "))


# злити в одну функцію check_string


def check_operator(potential_op):
    available_operators = [symbol.value for symbol in Button]
    if potential_op not in available_operators:
        write_to_output("Помилка. Введіть знак ще раз.")
        return check_operator(input("Введіть знак: "))
    return potential_op


def check_color(potential_color):
    available_colors = [symbol.value for symbol in Color]
    if potential_color not in available_colors:
        write_to_output("Помилка. Введіть колір ще раз.")
        return check_color(input("Введіть колір: "))
    return potential_color
