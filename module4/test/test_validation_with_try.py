"""
Program: test_validation_with_try.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to contain
unit tests for average_scores.py.
"""
import unittest
from module4.input_validation.validation_with_try import average


class FunctionTestCase(unittest.TestCase):
    def test_average_exception_first_score(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

    def test_average_exception_second_score(self):
        with self.assertRaises(ValueError):
            average(90, - 89, 78)
