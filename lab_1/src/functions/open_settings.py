from AppSettings import set_decimal, set_console_color

def open_settings():
    while True:
        print('1. Змінити кількість знаків після коми')
        print('2. Змінити колір тексту')
        print('3. Назад')

        answer = input()

        match answer:
            case '1':
                places = int(input('Введіть кількість знаків після коми: '))
                set_decimal(places)
                print(f'Кількість знаків після коми змінено на {places}.')
            case '2':
                print('Доступні кольори: black, red, green, yellow, blue, magenta, cyan, white')
                color = input('Введіть колір: ')
                set_console_color(color)
                print(f'Колір тексту змінено на {color}.')
            case '3':
                break
            case _:
                print('Такого варіанта меню не існує.')
