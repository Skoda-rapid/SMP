from shared.logger import Logger
from .BLL.ascii_art_creator import generate_ascii_art  # Додайте цей рядок

def main():
    Logger.log("Лабораторна 3 запущена")
    
    user_text = input("Введіть текст для ASCII-арту: ")

    print("Доступні шрифти:")
    fonts = ["slant", "block", "bubble", "digital"]
    for i, font in enumerate(fonts, 1):
        print(f"{i}. {font}")
    font_choice = int(input("Оберіть номер шрифту: "))
    font = fonts[font_choice - 1]

    print("Доступні кольори:\nred\ngreen\nblue\nyellow\ncyan\nmagenta")
    color = input("Введіть колір: ").strip().lower()

    symbol = input(
        "Введіть символ для ASCII-арту (або залиште пустим для стандартного): "
    )

    try:
        width_input = input(
            "Введіть бажану ширину ASCII-арту (або залиште пустим для стандартної ширини): "
        )
        width = int(width_input) if width_input else None
    except ValueError:
        width = None

    try:
        scale = int(
            input(
                "Введіть бажаний масштаб (1 для стандартного розміру, 2 для подвоєння, і т.д.): "
            )
        )
    except ValueError:
        scale = 1

    # Виклик функції для генерації ASCII-арту
    ascii_art = generate_ascii_art(user_text, font, color, symbol, width, scale)
    print(ascii_art)

    # Зберегти ASCII-арт у файл
    save_choice = input("Зберегти ASCII-арт у файл? (y/n): ").strip().lower()
    if save_choice == "y":
        file_path = input("Введіть назву файлу для збереження: ").strip()
        with open(file_path, "w") as file:
            file.write(ascii_art)
        print(f"ASCII-арт збережено у файл {file_path}.")
