from enum import Enum
from BLL.operations_functions import (
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
