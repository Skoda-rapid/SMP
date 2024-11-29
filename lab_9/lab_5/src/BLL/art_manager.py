import os
import sys

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if lab5_root not in sys.path:
    sys.path.insert(0, os.path.join(lab5_root, "shared"))

from shared.classes.art_generator.shape_generator import ShapeGenerator
from shared.classes.art_generator.text_generator import TextGenerator


class ArtManager:
    def create_text_art(self, params):
        return TextGenerator(**params)

    def create_shape(self, shape_type, size, symbol):
        return ShapeGenerator(shape_type, size, symbol)

    def generate_art(self, art_instance):
        return art_instance.generate()
