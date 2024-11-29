from colorama import Fore, Style

class ColorManager:
    COLORS = {
        "1": Fore.RED,
        "2": Fore.GREEN,
        "3": Fore.BLUE,
        "4": Fore.CYAN,
        "5": Fore.MAGENTA,
        "6": Fore.YELLOW,
        "7": Fore.WHITE
    }

    @staticmethod
    def choose_color():
        print("Доступні кольори:")
        for key, color in ColorManager.COLORS.items():
            print(f"{key}: {color}{color.upper()}{Style.RESET_ALL}")
        choice = input("Виберіть номер кольору (за замовчуванням білий): ") or "7"
        return ColorManager.COLORS.get(choice, Fore.WHITE)
