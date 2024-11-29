
import os
import sys

shared_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, shared_root)


from .ascii_art_generator import ArtGenerator
from shapes import Cube, Sphere


class ShapeGenerator(ArtGenerator):
    def __init__(self, shape_type, size=5, symbol="*"):
        super().__init__(symbol)
        self.shape_type = shape_type
        self.size = size

    def generate(self):
        if self.shape_type == "cube":
            shape = Cube(self.size, self.symbol)
        elif self.shape_type == "sphere":
            shape = Sphere(self.size, self.symbol)
        else:
            raise ValueError("Unsupported shape type.")

        return shape.draw()
