from functions.input_operator import input_operator
from functions.input_number import input_number
from functions.calc_result import calc_result
from functions.history import add_to_history
from AppSettings import get_decimal

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
