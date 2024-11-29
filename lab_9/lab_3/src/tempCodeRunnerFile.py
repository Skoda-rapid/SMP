def get_user_text():
    return input("Введіть текст для ASCII-арту: ")

def get_user_font():
    fonts = ['slant', 'block', 'bubble', 'digital']
    print("Доступні шрифти:")
    for i, font in enumerate(fonts):
        print(f"{i + 1}. {font}")
    choice = int(input("Оберіть номер шрифту: ")) - 1
    return fonts[choice] if 0 <= choice < len(fonts) else 'slant'

def get_user_color():
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    print("Доступні кольори:")
    for color in colors:
        print(color)
    color = input("Введіть колір: ").lower()
    return color if color in colors else None

def get_user_symbol():
    return input("Введіть символ для ASCII-арту (або залиште пустим для стандартного): ") or None

def get_user_confirmation(prompt):
    return input(prompt).strip().lower() == 'так'

# Нова функція для введення ширини
def get_user_width():
    width = input("Введіть бажану ширину ASCII-арту (або залиште пустим для стандартної ширини): ")
    return int(width) if width.isdigit() else 80  # Повертає 80 за замовчуванням
