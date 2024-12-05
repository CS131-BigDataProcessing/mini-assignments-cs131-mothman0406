# unitTest_math_functions.py

import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    # Edge cases for power function
    def test_zero_power(self):
        self.assertEqual(power(2, 0), 1)  # Any number raised to 0 should be 1

    def test_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)  # Negative exponent should give a fraction

    def test_zero_base(self):
        self.assertEqual(power(0, 5), 0)  # Zero raised to any power should be zero

    # Edge cases for divide function
    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            divide(5, 0)  # Dividing by zero should raise ValueError

    def test_positive_division(self):
        self.assertEqual(divide(10, 2), 5)  # Normal division

    def test_negative_division(self):
        self.assertEqual(divide(10, -2), -5)  # Negative divisor

if __name__ == "__main__":
    unittest.main()

