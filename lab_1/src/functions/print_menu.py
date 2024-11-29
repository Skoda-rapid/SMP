# print_menu.py
from functions.calculate import calculate
from functions.open_settings import open_settings
from functions.show_history import show_history
from functions.memory import memory_clear, memory_recall, memory_store, memory_add
from AppSettings import get_console_color

def print_menu():
    while True:
        color = get_console_color()
        print(color + '1. Обчислити')
        print(color + '2. Історія')
        print(color + '3. Налаштування')
        print(color + '4. Пам\'ять')
        print(color + '5. Вийти')

        answer = input()

        match answer:
            case '1':
                calculate()
            case '2':
                show_history()
            case '3':
                open_settings()
            case '4':
                memory_menu()
            case '5':
                break
            case _:
                print('Такого варіанта меню не існує.')

def memory_menu():
    while True:
        color = get_console_color()
        print(color + '1. Очистити пам\'ять')
        print(color + '2. Викликати пам\'ять')
        print(color + '3. Зберегти в пам\'ять')
        print(color + '4. Додати до пам\'яті')
        print(color + '5. Назад')

        answer = input()

        match answer:
            case '1':
                memory_clear()
                print("Пам'ять очищена.")
            case '2':
                print(f"Значення в пам'яті: {memory_recall()}")
            case '3':
                value = float(input("Введіть значення для збереження: "))
                memory_store(value)
                print("Значення збережено.")
            case '4':
                value = float(input("Введіть значення для додавання: "))
                memory_add(value)
                print("Значення додано.")
            case '5':
                break
            case _:
                print('Такого варіанта меню не існує.')
