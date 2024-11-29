import pyfiglet

class AsciiArtGenerator:
    def __init__(self, text, font, width=80):
        self.text = text
        self.font = font
        self.width = width

    def generate(self):
        ascii_art = pyfiglet.Figlet(font=self.font, width=self.width)
        return ascii_art.renderText(self.text)
