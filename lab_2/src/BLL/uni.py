import unittest
from unittest.main import main
from operations_functions import add, 

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.add(5, 3), 8)
        self.assertEqual(Calculator.add(-5, 3), -2)
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(-5, 3), -8)
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(-5, -3), -2)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(5, 3), 15)
        self.assertEqual(Calculator.multiply(-5, 3), -15)
        self.assertEqual(Calculator.multiply(5, 0), 0)
        self.assertEqual(Calculator.multiply(-5, -3), 15)

    def test_division(self):
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertEqual(Calculator.divide(-6, 3), -2)
        self.assertEqual(Calculator.divide(-6, -3), 2)
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            Calculator.add("a", 5)
        with self.assertRaises(ValueError):
            Calculator.subtract(5, "b")
        with self.assertRaises(ValueError):
            Calculator.multiply("x", "y")
        with self.assertRaises(ValueError):
            Calculator.divide(5, "z")

if __name__ == "__main__":
    main()