from ..UI.input_operator import input_operator
from ..UI.input_number import input_number
from .calc_result import calc_result
from .history import add_to_history
from ...AppSettings import get_decimal

def calculate():
    number1 = input_number()
    operator = input_operator()

    if operator == "sqrt":
        result = calc_result(number1, operator)
        expression = f"{operator}({number1})"
    else:
        number2 = input_number()
        result = calc_result(number1, operator, number2)
        expression = f"{number1} {operator} {number2}"

    decimal_places = get_decimal()
    result = round(result, decimal_places)
    add_to_history(expression, result)
    print(f"Result is: {result:.{decimal_places}f}")
