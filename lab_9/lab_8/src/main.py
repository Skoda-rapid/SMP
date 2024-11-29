
import os
import sys
from shared.logger import Logger


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from .UI.console.ConsoleUI import ConsoleUI


def main():
    Logger.log("Лабораторна 1 запущена")
    
    ui = ConsoleUI()
    ui.display_menu()
