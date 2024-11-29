from constants.GlobalVariables import Button

def check_operator(potential_op):

    while True:
        available_operators = [symbol.value for symbol in Button]

        if potential_op not in available_operators:
            potential_op = input('Помилка. Введіть знак ще раз: ')
        else:
            break

    return potential_op
