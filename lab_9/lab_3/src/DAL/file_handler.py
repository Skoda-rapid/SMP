def save_to_file(ascii_art, filename):
    with open(f"{filename}.txt", "w") as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файлі {filename}.txt")
