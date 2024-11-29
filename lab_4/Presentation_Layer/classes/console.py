from Business_Layer.classes.ascii import Ascii
from Shared.classes.validators import Validators


class Console:
    def __init__(self):
        self.ascii = Ascii("", color="random")
        self.__prompt()

    def __prompt(self):
        self.ascii.print()
        self.ascii.color = "\033[39m"
        while True:
            prompt = input("1 - Enter text\n"
                           "2 - Change font's symbols\n"
                           "3 - Change width and height\n"
                           "4 - Change color\n"
                           "5 - Change text orientation\n"
                           "Your choice: ")
            Validators.validate_main_prompt(prompt, self)

    def enter_text(self):
        text = input("Enter text: ")
        self.ascii.text = text
        ftext = self.ascii.print()
        save_prompt = input("Do you want to save the text? (y/n): ").lower()
        Validators.validate_main_prompt(save_prompt, ftext)

    def change_symbols(self):
        shadow_prompt = input("Enter symbol for shadows: ")
        Validators.validate_shading(shadow_prompt, self, 1)
        text_prompt = input("Enter symbol for text: ")
        Validators.validate_shading(text_prompt, self, 2)
        highlight_prompt = input("Enter symbol for highlights: ")
        Validators.validate_shading(highlight_prompt, self, 3)

    def change_width_and_height(self):
        width_prompt = input("Enter the width of an ASCII art\n"
                  "(any non-positive value will reset it to default values\n"
                  "Your choice: ")
        Validators.validate_main_prompt(width_prompt, self)
        height_prompt = input("Enter the height of an ASCII art\n"
                              "(any non-positive value will reset it to default values\n"
                              "Your choice: ")
        Validators.validate_main_prompt(height_prompt, self)

    def change_color(self):
        color_prompt = input("Enter the color of your ASCII art:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Yellow\n"
                             "4 - Blue\n"
                             "5 - Magenta\n"
                             "6 - Cyan\n"
                             "7 - Light gray\n"
                             "8 - Random\n"
                             "0 - Default\n"
                             "Your choice: ")
        Validators.validate_color(color_prompt, self)

    def justify(self):
        justify_prompt = input("Enter the orientation of your ASCII art:\n"
                               "1 - Left\n"
                               "2 - Center\n"
                               "3 - Right\n"
                               "Your choice: ")
        Validators.validate_justify(justify_prompt, self)