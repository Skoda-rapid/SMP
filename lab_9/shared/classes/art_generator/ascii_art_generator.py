# from shared.libs.font_library import get_ascii_font


class ArtGenerator:
    def __init__(self, art_type, symbol="*", width=40, height=10, alignment="center", color_mode="bw"):
        self.type = art_type
        self.symbol = symbol
        self.width = width
        self.height = height
        self.alignment = alignment
        self.color_mode = color_mode

    def generate(self):
        raise NotImplementedError("Subclasses must implement the generate method.")
