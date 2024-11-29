import pandas as pd
from colorama import Fore, Back, Style

class UserInterface:
    def display_table(self, data):
        try:
            df = pd.DataFrame(data)
            # Виведення таблиці з зеленою підсвіткою
            print(Fore.GREEN + df.to_string(index=False) + Fore.RESET)
        except Exception as e:
            print(Fore.RED + "Помилка при відображенні таблиці: " + str(e) + Fore.RESET)

    def get_user_input(self, prompt, input_type=str):
        while True:
            try:
                user_input = input(prompt)
                if input_type == int:
                    return int(user_input)
                elif input_type == float:
                    return float(user_input)
                return user_input
            except ValueError:
                print(Fore.YELLOW + "Невірний ввід, будь ласка, спробуйте знову." + Fore.RESET)

    def show_message(self, message, message_type="info"):
        if message_type == "info":
            print(Fore.CYAN + message + Fore.RESET)
        elif message_type == "error":
            print(Fore.RED + message + Fore.RESET)
        elif message_type == "success":
            print(Fore.GREEN + message + Fore.RESET)
        else:
            print(message)
