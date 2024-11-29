import textwrap
from shared.libs.font_library import get_ascii_font
from .ascii_art_generator import ArtGenerator

class TextGenerator(ArtGenerator):
    def __init__(self, text, symbol="*", width=40, height=10, alignment="center", color_mode="bw"):
        # Викликаємо конструктор батьківського класу ArtGenerator
        super().__init__("text", symbol, width, height, alignment, color_mode)
        self.text = text

    def generate(self):
        font = get_ascii_font(self.symbol)
        base_height = 5
        max_chars_per_line = self.width
        wrapped_text = textwrap.wrap(str(self.text), max_chars_per_line)
        ascii_art_lines = []

        for line in wrapped_text:
            lines = [""] * base_height
            for char in line.upper():
                if char in font:
                    char_lines = font[char]
                    for i in range(base_height):
                        lines[i] += char_lines[i] + " "
                else:
                    for i in range(base_height):
                        lines[i] += " " * 6

            for i in range(len(lines)):
                if self.alignment == "center":
                    lines[i] = lines[i].center(self.width)
                elif self.alignment == "right":
                    lines[i] = lines[i].rjust(self.width)
                else:
                    lines[i] = lines[i].ljust(self.width)

            ascii_art_lines.extend(lines)

        if self.height < len(ascii_art_lines):
            ascii_art_lines = ascii_art_lines[: self.height]

        if self.color_mode == "gray":
            ascii_art_lines = [
                line.replace(self.symbol, "\033[90m" + self.symbol + "\033[0m")
                for line in ascii_art_lines
            ]

        return "\n".join(ascii_art_lines)
