from unittest import TestCase
from and_or import *


class Test(TestCase):
    def test_between_zero_and_one_true(self):
        self.assertEqual(between_zero_and_one(1), 1)

    def test_between_zero_and_one_false(self):
        self.assertEqual(between_zero_and_one(1), 0.1)

    def test_integer_or_float_integer_input(self):
        self.assertEqual(integer_or_float(5), 0.0)

    def test_integer_or_float_float_input(self):
        self.assertEqual(integer_or_float(0.0), 5)

    def test_integer_or_float_string_input(self):
        self.assertEqual(integer_or_float(77), None)

    def test_integer_or_float_boolean_input(self):
        self.assertEqual(integer_or_float(True), None)