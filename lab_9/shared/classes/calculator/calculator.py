"""
Модуль `calculator.py` реалізує клас `Calculator`, який забезпечує базові функції калькулятора, 
такі як арифметичні операції, управління пам'яттю та ведення історії.
"""

import shared.functions.manage_app_settings as manage_app_settings
from shared.constants.global_variables import Button, operations
from shared.logger import Logger


class Calculator:
    """
    Клас `Calculator` забезпечує функціональність для виконання математичних операцій,
    управління пам'яттю та ведення історії обчислень.

    Атрибути:
        current_value (float): Поточне значення калькулятора.
        memory (float): Значення, збережене в пам'яті калькулятора.
        history (list): Список, який містить історію виконаних операцій.
        decimal_places (int): Кількість знаків після коми для відображення результату.
    """

    def __init__(self, current_value=0, memory=0):
        """
        Ініціалізує екземпляр класу Calculator.

        Args:
            current_value (float): Початкове значення калькулятора (за замовчуванням 0).
            memory (float): Початкове значення пам'яті калькулятора (за замовчуванням 0).
        """
        self.current_value = current_value
        self.memory = memory
        self.history = []
        self.decimal_places = manage_app_settings.decimal_places

    def validate_number(self, value):
        """
        Перевіряє, чи є введене значення числом.

        Args:
            value: Значення для перевірки.

        Returns:
            float: Перетворене числове значення.

        Raises:
            ValueError: Якщо введене значення не є числом.
        """
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Помилка. Введене значення не є числом")

    def validate_operator(self, operator):
        """
        Перевіряє, чи є введений оператор коректним.

        Args:
            operator (str): Оператор для перевірки.

        Returns:
            str: Перевірений оператор.

        Raises:
            ValueError: Якщо оператор некоректний.
        """
        if not operator in {button.value for button in Button}:
            raise ValueError(f"Введено некоректний оператор.")
        return operator

    def calc(self, number_1, operator, number_2=None):
        """
        Виконує математичну операцію на основі введених чисел та оператора.

        Args:
            number_1 (float): Перше число.
            operator (str): Оператор для виконання операції.
            number_2 (float, optional): Друге число (для унарних операторів не потрібне).

        Returns:
            float: Результат операції.

        Raises:
            ValueError: Якщо операція не може бути виконана.
        """
        try:
            if operator == Button.SQRT.value:
                Logger.log(f"{number_1} {operator} {number_2}")
                return operations[operator](number_1)
            else:
                return operations[operator](number_1, number_2)
        except Exception as e:
            raise ValueError(f"Помилка виконання операції: {e}")

    def add_to_history(self, param_1, operator, param_2, result):
        """
        Додає виконану операцію до історії.

        Args:
            param_1 (float): Перше число.
            operator (str): Використаний оператор.
            param_2 (float): Друге число.
            result (float): Результат виконаної операції.
        """
        if operator == Button.SQRT:
            self.history.append(f"{operator} {param_1} = {result}")

        self.history.append(f"{param_1} {operator} {param_2} = {result}")

    def add_to_memory(self, param):
        """
        Додає число до пам'яті калькулятора.

        Args:
            param (float): Число, яке потрібно додати до пам'яті.

        Raises:
            ValueError: Якщо введене значення не є числом.
        """
        number = self.validate_number(param)
        print(number + self.memory)
