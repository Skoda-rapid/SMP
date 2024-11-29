import BLL.manage_app_settings as manage_app_settings
from shared.classes.ConsoleReader import ConsoleReader
from shared.classes.Calculator import Calculator
from shared.classes.ConsoleWriter import ConsoleWriter
from shared.constants.global_variables import main_menu, memory_menu, settings_menu
from UI.menu_functions import print_menu


class CalculatorConsole:
    def __init__(self):
        self.consoleWriter = ConsoleWriter()
        self.consoleReader = ConsoleReader()
        self.calculator = Calculator()

    def run_console(self):

        while True:
            print_menu(manage_app_settings.console_color, main_menu)
            answer = self.consoleReader.input_data("Оберіть варіант меню")

            match answer:
                case 1:
                    self.handle_calc()
                case 2:
                    self.consoleWriter.output_value(
                        self.calculator.current_value, "Відповідь"
                    )

                case 3:
                    self.consoleWriter.output_value(self.calculator.history, "Історія")

                case 4:
                    self.handle_settings_menu()

                case 5:
                    self.handle_memory_menu()

                case 6:
                    break

                case _:
                    self.consoleWriter.output_value(
                        answer, "Такого варіанта в меню немає"
                    )
            continue_answer = self.consoleReader.read_value("Продовжити? (так/ні)")
            if continue_answer == "ні":
                break

    def handle_calc(self):
        param_1 = self.consoleReader.input_data("Введіть перше число")
        operator = self.consoleReader.input_data("Введіть оператор", "operator")
        param_2 = self.consoleReader.input_data("Введть друге число")

        result = self.calculator.calc(param_1, operator, param_2)
        result = round(result, int(manage_app_settings.decimal_places))

        self.calculator.current_value = result
        self.calculator.add_to_history(param_1, operator, param_2, result)

    def handle_settings_menu(self):
        while True:
            print_menu(manage_app_settings.console_color, settings_menu)
            option = self.consoleReader.input_data("Оберіть варіант меню")
            match option:
                case 1:
                    new_decimal = self.consoleReader.input_data(
                        "Введіть нову кількість знаків після коми"
                    )

                    manage_app_settings.set_decimal(new_decimal)
                    self.consoleWriter.output_value(
                        manage_app_settings.decimal_places,
                        "Кількість знаків після коми змінено на",
                    )

                case 2:
                    self.consoleWriter.output_value(
                        manage_app_settings.console_color, "Поточний колір консолі"
                    )
                    new_color = self.consoleReader.input_data(
                        """Введіть новий колір.
                            Доступні кольори:
                            black, red, green, yellow, blue, magenta, cyan, white
                        """,
                        "color",
                    )
                    manage_app_settings.set_console_color(new_color)
                    self.consoleWriter.output_value(
                        manage_app_settings.console_color, "Колір консолі змінено на"
                    )

                case 3:
                    break

                case _:
                    self.consoleWriter.output_value(
                        option, "Такого ваіанта в меню немає"
                    )

    def handle_memory_menu(self):
        while True:
            print_menu(manage_app_settings.console_color, memory_menu)

            option = self.consoleReader.input_data("Оберіть варіант меню")

            match option:
                case 1:
                    self.calculator.memory = 0
                case 2:
                    self.consoleWriter.output_value(
                        self.calculator.memory, "Поточне значення"
                    )
                case 3:
                    self.calculator.memory = self.consoleReader.input_data(
                        "Введіть нове значення пам'яті"
                    )
                case 4:
                    new_value = self.consoleReader.input_data(
                        "Додати в пам'ять таке значення"
                    )

                    self.calculator.memory += new_value

                case 5:
                    break
                case _:
                    self.consoleWriter.output_value(
                        option, "Такого ваіанта в меню немає"
                    )
