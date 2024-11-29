import pyfiglet

class FontManager:
    @staticmethod
    def choose_font():
        available_fonts = pyfiglet.FigletFont.getFonts()  # Отримання списку шрифтів
        print("Доступні шрифти:")
        for i, font in enumerate(available_fonts[:20], start=1):  # Відображення перших 20 шрифтів
            print(f"{i}: {font}")
        choice = int(input("Виберіть номер шрифту (за замовчуванням 1): ") or 1)
        return available_fonts[choice - 1] if 1 <= choice <= len(available_fonts) else "standard"
