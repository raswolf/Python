"""
Program: test_operators_practice.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to contain
unit tests investigating various operators.
"""

import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(5 == 5)

    def test_equal_false(self):
        self.assertFalse(7 == 5)

    def test_not_equal(self):
        self.assertTrue('e' != 5)

    def test_not_equal_false(self):
        self.assertFalse('e' != 'e')

    def test_greater_than(self):
        self.assertTrue(8 > 5)

    def test_greater_than_false(self):
        self.assertFalse(8 > 12)

    def test_less_than(self):
        self.assertTrue(5 < 8)

    def test_less_than_false(self):
        self.assertFalse(12 < 8)

    def test1_greater_or_equal(self):
        self.assertTrue(8 >= 5)

    def test2_greater_or_equal(self):
        self.assertTrue(8 >= 8)

    def test_greater_or_equal_false(self):
        self.assertFalse(8 >= 12)

    def test1_less_or_equal(self):
        self.assertTrue(5 <= 8)

    def test2_less_or_equal(self):
        self.assertTrue(5 <= 5)

    def test_less_or_equal_false(self):
        self.assertFalse(12 <= 8)


if __name__ == '__main__':
    unittest.main()
