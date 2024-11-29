import os
import sys

from shared.logger import Logger

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab4_root)
from shared.classes.art_generator.ascii_art_generator import ArtGenerator
from shared.classes.art_generator.console_reader import ConsoleReader
from shared.classes.art_generator.console_writer import ConsoleWriter
from shared.classes.art_generator.file_writer import FileWriter


def main():
    Logger.log("Лабораторна 4 запущена")
    
    text = ConsoleReader.read_text()
    symbol = ConsoleReader.read_symbol_set()
    width = ConsoleReader.read_width()
    height = ConsoleReader.read_height()
    alignment = ConsoleReader.read_alignment()
    color_mode = ConsoleReader.read_color_mode()

    art_generator = ArtGenerator(text, symbol, width, height, alignment, color_mode)
    ascii_art = art_generator.generate()

    ConsoleWriter.display_art(ascii_art)

    save_to_file = (
        input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
    )
    if save_to_file == "так":
        filename = input(
            "Введіть назву файлу (за замовчуванням 'ascii_art.txt'): "
        ).strip()
        filename = filename if filename else "ascii_art.txt"
        FileWriter.save_art_to_file(ascii_art, filename)
