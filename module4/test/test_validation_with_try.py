"""
Program: test_validation_with_try.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to contain
unit tests for average_scores.py.
"""
import unittest
from module3.format_output.average_scores import average


class FunctionTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

