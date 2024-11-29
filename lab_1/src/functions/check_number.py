def check_number(num):
    while not num.isnumeric():
        num = input('Помилка. Введіть число: ')
    return float(num)
