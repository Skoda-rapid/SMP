def preview_art(ascii_art):
    print("Попередній перегляд:")
    print(ascii_art)
    confirm = input("Чи хочете зберегти? (y/n): ").lower()
    return confirm == "y"
