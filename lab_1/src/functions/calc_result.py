from constants.GlobalVariables import Button
from functions.operations_functions import *

def calc_result(num1, oper, num2=0):
    a = float(num1)
    b = float(num2)

    operations = {
        Button.ADDITION.value: add,
        Button.SUBTRACTION.value: subtract,
        Button.MULTIPLICATION.value: multiply,
        Button.DIVISION.value: divide,
        Button.SQRT.value: find_sqrt,
        Button.REMAINDER.value: find_remainder,
        Button.POWER.value: to_power
    }

    if oper in operations:
        if oper == Button.SQRT.value:
            return operations[oper](a)
        else:
            return operations[oper](a, b)
    else:
        return "Неправильний оператор"