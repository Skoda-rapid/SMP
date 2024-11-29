from shared.logger import Logger
import sys
import os
import unittest

lab2_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab2_root)

main_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(main_root)

from shared.classes.calculator.сalculator_сonsole import CalculatorConsole


def main():
    Logger.log("Лабораторна 2 запущена")

    console = CalculatorConsole()
    console.run_console()
    unittest.main()
