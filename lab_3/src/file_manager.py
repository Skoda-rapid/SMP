class FileManager:
    @staticmethod
    def save_to_file(ascii_art):
        file_name = input("Введіть ім'я файлу для збереження (за замовчуванням art.txt): ") or "art.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(ascii_art)
        print(f"ASCII-арт збережено у файл: {file_name}")
