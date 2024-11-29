from src.user_input import UserInput
from src.font_manager import FontManager
from src.color_manager import ColorManager
from src.ascii_art_generator import AsciiArtGenerator
from src.file_manager import FileManager
from src.display_manager import DisplayManager

class AsciiArtApp:
    def __init__(self):
        self.text = ""
        self.font = "standard"
        self.color = ColorManager.COLORS["7"]
        self.width = 80
        self.ascii_art = ""

    def run(self):
        print("ASCII ART Генератор")
        
        # Введення тексту
        self.text = UserInput.get_text()
        
        # Вибір шрифту
        self.font = FontManager.choose_font()
        
        # Вибір кольору
        self.color = ColorManager.choose_color()
        
        # Вибір ширини
        self.width = int(input("Вкажіть ширину для ASCII-арту (за замовчуванням 80): ") or 80)
        
        # Генерація ASCII-арту
        generator = AsciiArtGenerator(self.text, self.font, self.width)
        self.ascii_art = generator.generate()
        
        # Попередній перегляд
        DisplayManager.preview(self.ascii_art, self.color)
        
        # Збереження у файл
        save = input("Бажаєте зберегти результат у файл? (так/ні): ").lower()
        if save == "так":
            FileManager.save_to_file(self.ascii_art)

if __name__ == "__main__":
    app = AsciiArtApp()
    app.run()
