"""
Модуль для запису в консоль виведення результатів калькулятора.
Визначає функції для відображення інформації користувачеві.
"""

from shared.functions.ui_functions.handle_input import write_to_output


class ConsoleWriter:
    """
    Клас для запису інформації в консоль.

    Містить методи для виведення результатів обчислень користувачу.
    """

    def output_value(self, value, message="Ваше значення"):
        """
        Виводить результат в консоль.

        Параметри:
            output (str): Результат обчислення для виведення.
        """
        write_to_output(f"{message}: {value}")
