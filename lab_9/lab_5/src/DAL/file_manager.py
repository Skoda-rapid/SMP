import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, os.path.join(project_root, "shared"))

from shared.classes.art_generator.ascii_art_generator import ArtGenerator

class FileArtGenerator(ArtGenerator):
    def __init__(self, text, symbol="*", width=40, height=10, alignment="center", color_mode="bw", filename="output.txt"):
        super().__init__(text, symbol, width, height, alignment, color_mode)
        self.filename = filename

    def generate_and_save(self):
        ascii_art = self.generate()
        with open(self.filename, "w") as file:
            file.write(ascii_art)
        print(f"ASCII art saved to {self.filename}")
