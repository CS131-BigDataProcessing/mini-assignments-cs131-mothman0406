# unit_test.py
import unittest
from validate_functions import validate_sex, validate_age
from stats_function import calculate_mean, calculate_median

class TestCrimeFunctions(unittest.TestCase):
    
    # Test validate_sex function
    def test_validate_sex_valid(self):
        self.assertTrue(validate_sex('M'))
        self.assertTrue(validate_sex('F'))

    def test_validate_sex_invalid(self):
        with self.assertRaises(ValueError):
            validate_sex('X')
        with self.assertRaises(ValueError):
            validate_sex(None)

    # Test validate_age function
    def test_validate_age_valid(self):
        self.assertTrue(validate_age(25))
        self.assertTrue(validate_age(1))
        self.assertTrue(validate_age(100))

    def test_validate_age_invalid(self):
        with self.assertRaises(ValueError):
            validate_age(0)
        with self.assertRaises(ValueError):
            validate_age(101)
        with self.assertRaises(ValueError):
            validate_age(None)

    # Test stats_function functions
    def test_calculate_mean(self):
        ages = [20, 30, 40, 50]
        self.assertEqual(calculate_mean(ages), 35)

    def test_calculate_median(self):
        ages = [20, 30, 40, 50, 60]
        self.assertEqual(calculate_median(ages), 40)
        ages = [20, 30, 40, 50]
        self.assertEqual(calculate_median(ages), 35)

if __name__ == "__main__":
    unittest.main()

