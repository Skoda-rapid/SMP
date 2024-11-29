from shared.classes.art_generator.console_reader import ConsoleReader
from shared.classes.art_generator.console_writer import ConsoleWriter
from shared.classes.art_generator.ascii_art_generator import ArtGenerator
from shared.functions import manage_app_settings
from shared.functions.ui_functions.menu_functions import print_menu
from shared.constants.global_variables import art_menu


class ArtConsole:
    def __init__(self):
        self.console_writer = ConsoleWriter()
        self.console_reader = ConsoleReader()
        self.art_generator = ArtGenerator()

    def run_console(self, art_type):
        while True:
            print_menu(manage_app_settings.console_color, art_menu)
            answer = self.console_reader.input_data("Оберіть варіант меню")

