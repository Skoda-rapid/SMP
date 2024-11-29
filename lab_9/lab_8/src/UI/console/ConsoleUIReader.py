
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", '..', '..'))
sys.path.append(project_root)

from shared.functions.ui_functions.handle_input import read_from_input

class ConsoleUIReader:
    def console_read(self, message=""):
        user_input = read_from_input(message)
        return user_input