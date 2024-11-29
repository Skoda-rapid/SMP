def save_to_file(ascii_art, filename="ascii_art.txt"):
    with open(filename, "w") as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл {filename}")
