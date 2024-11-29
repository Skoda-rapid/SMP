class FileWriter:
    def save_art_to_file(art, filename="ascii_art.txt"):
        with open(filename, "w") as file:
            file.write(art)
        print(f"ASCII-арт збережено у файл {filename}")
