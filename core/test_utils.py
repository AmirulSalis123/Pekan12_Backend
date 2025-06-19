from django.test import TestCase
from core.utils import calculator, validate_password

class CalculatorTest(TestCase):
    def test_addition(self):
        self.assertEqual(calculator(2, 3, '+'), 5)

    def test_subtraction(self):
        self.assertEqual(calculator(5, 2, '-'), 3)

    def test_multiplication(self):
        self.assertEqual(calculator(3, 4, 'x'), 12)

    def test_division(self):
        self.assertEqual(calculator(10, 2, '/'), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator(5, 0, '/')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculator(3, 4, '%')

class PasswordValidationTest(TestCase):
    def test_valid_password(self):
        self.assertTrue(validate_password("Password1!"))

    def test_invalid_too_short(self):
        self.assertFalse(validate_password("P1!a"))

    def test_no_uppercase(self):
        self.assertFalse(validate_password("password1!"))

    def test_no_lowercase(self):
        self.assertFalse(validate_password("PASSWORD1!"))

    def test_no_digit(self):
        self.assertFalse(validate_password("Password!"))

    def test_no_special_char(self):
        self.assertFalse(validate_password("Password1"))