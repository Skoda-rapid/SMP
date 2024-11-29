from shared.logger import Logger
import os
import sys

lab1_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab1_root)

from .UI.print_menu import *


def main():
    Logger.log("Лабораторна 1 запущена")
    print_menu()
