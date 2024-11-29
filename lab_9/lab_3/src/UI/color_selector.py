def choose_color():
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "default": "\033[0m"
    }
    print("Доступні кольори:", ", ".join(colors.keys()))
    color = input("Оберіть колір: ").lower()
    return colors.get(color, "\033[0m")  # Повертає вибраний колір або скидає до стандартного
