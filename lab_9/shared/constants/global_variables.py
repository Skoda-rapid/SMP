from enum import Enum
from shared.functions.operations_functions import (
    add,
    subtract,
    multiply,
    divide,
    find_sqrt,
    find_remainder,
    to_power,
)


class Button(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"
    SQRT = "sqrt"
    REMAINDER = "%"
    POWER = "^"


from enum import Enum


class Color(Enum):
    BLACK = "black"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "white"


operations = {
    Button.ADDITION.value: add,
    Button.SUBTRACTION.value: subtract,
    Button.MULTIPLICATION.value: multiply,
    Button.DIVISION.value: divide,
    Button.SQRT.value: find_sqrt,
    Button.REMAINDER.value: find_remainder,
    Button.POWER.value: to_power,
}

main_menu = """
1. Ввести дані
2. Вивести результат
3. Історія
4. Налаштування
5. Пам'ять
6. Вийти
"""

memory_menu = """
1. Очистити пам'ять
2. Викликати пам'ять
3. Зберегти в пам'ять
4. Додати до пам'яті
5. Назад
"""

settings_menu = """
1. Змінити кількість знаків після коми
2. Змінити колір тексту
3. Назад
"""

art_menu = """
1. Ввести тип арту (text, shape)
2. Ввести бажаний символ
3. Вивести арт
4. Зберегти арт у файл
5. Вийти
"""

text_menu = """
1. 
"""

shape_menu = """
"""
# shared\constants\global_variables.py
csv_menu = """
1. Працювати з візуалізацією
2. Вийти 
"""

criteria_menu = """
1. Вивести екстремальні значення по стовцях
2. Відфільтрувати дані за критерієм
3. Візуалізувати дані (graphic / bar)
4. Додати графік
5. Експортувати як png
6. Вийти
"""

labs_menu = """
1. Лабораторна №1
2. Лабораторна №2
3. Лабораторна №3
4. Лабораторна №4
5. Лабораторна №5
7. Лабораторна №7
8. Лабораторна №8
0. Вихід"
"""
