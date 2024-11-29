import BLL.manage_app_settings as manage_app_settings
from shared.constants.global_variables import Button, operations


class Calculator:

    def __init__(self, current_value=0, memory=0):
        self.current_value = current_value
        self.memory = memory
        self.history = []
        self.decimal_places = manage_app_settings.decimal_places

    def validate_number(self, value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Помилка. Введене значення не є числом")

    def validate_operator(self, operator):
        if not operator in {button.value for button in Button}:
            raise ValueError(f"Введено некоректний оператор.")
        return operator

    def calc(self, number_1, operator, number_2=None):
        try:
            if operator == Button.SQRT.value:
                return operations[operator](number_1)
            else:
                return operations[operator](number_1, number_2)
        except Exception as e:
            raise ValueError(f"Помилка виконання операції: {e}")

    def add_to_history(self, param_1, operator, param_2, result):
        if operator == Button.SQRT:
            self.history.append(f"{operator} {param_1} = {result}")

        self.history.append(f"{param_1} {operator} {param_2} = {result}")


    def add_to_memory(self, param):
        number = self.validate_number(param)

        print(number + self.memory)
