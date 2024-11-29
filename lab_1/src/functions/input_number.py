from functions.check_number import check_number

def input_number():
    number = input("Введіть число: ")
    number = check_number(number)

    return number