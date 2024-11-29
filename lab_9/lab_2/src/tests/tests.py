# tests/test_calculator.py
import os
import sys

lab2_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab2_root)
main_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(main_root)
# from src.BLL.main import main

import unittest
from shared.classes.calculator.сalculator_сonsole import CalculatorConsole


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculatorConsole = CalculatorConsole()
        self.calculator = self.calculatorConsole.calculator

    # Завдання 1: Тестування Додавання
    def test_add(self):
        self.assertEqual(self.calculatorConsole.calculator.calc(5, "+", 3), 8)
        self.assertEqual(self.calculatorConsole.calculator.calc(-2, "+", -3), -5)
        self.assertEqual(self.calculatorConsole.calculator.calc(0, "+", 0), 0)

    # Завдання 2: Тестування Віднімання
    def test_subtract(self):
        self.assertEqual(self.calculatorConsole.calculator.calc(10, "-", 5), 5)
        self.assertEqual(self.calculatorConsole.calculator.calc(-5, "-", -3), -2)
        self.assertEqual(self.calculatorConsole.calculator.calc(5, "-", 10), -5)

    # Завдання 3: Тестування Множення
    def test_multiply(self):
        self.assertEqual(self.calculatorConsole.calculator.calc(4, "*", 3), 12)
        self.assertEqual(self.calculatorConsole.calculator.calc(-2, "*", 3), -6)
        self.assertEqual(self.calculatorConsole.calculator.calc(0, "*", 5), 0)

    # Завдання 4: Тестування Ділення
    def test_divide(self):
        self.assertEqual(self.calculatorConsole.calculator.calc(10, "/", 2), 5)
        self.assertEqual(self.calculatorConsole.calculator.calc(-6, "/", 3), -2)
        self.assertAlmostEqual(
            self.calculatorConsole.calculator.calc(1, "/", 3), 0.333333, places=5
        )

        with self.assertRaises(ValueError):
            self.calculatorConsole.calculator.calc(10, "/", 0)

    # Завдання 5: Тестування Обробки Помилок
    def test_error_handling(self):

        with self.assertRaises(ValueError):
            self.calculatorConsole.calculator.calc(10, "/", 0)(
                10, 0
            )  


if __name__ == "__main__":
    unittest.main()
