"""
Program: test_coupon_calculations.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to contain
unit tests for coupon_calculations.py.
"""

import unittest
from module4.store.coupon_calculations import calculate_order


class FunctionTestCase(unittest.TestCase):
    """Tests operation with user input price = 10, cash_coupon = 5, percent_coupon = 10
    Shipping will be $5.95, tax is 6%"""
    def test1_set1(self):
        self.assertAlmostEqual(calculate_order(10, 5, 10), 11.05, places=4)

    """Tests operation with user input 10, 5, 15"""
    def test2_set1(self):
        self.assertAlmostEqual(calculate_order(10, 5, 15), 10.8, places=4)

    """Tests operation with user input 10, 5, 20 """
    def test3_set1(self):
        self.assertAlmostEqual(calculate_order(10, 5, 20), 10.55, places=4)

    """Tests operation with user input 10, 10, 10 """
    def test4_set1(self):
        self.assertAlmostEqual(calculate_order(10, 10, 10), 6.55, places=4)

    """Tests operation with user input 10, 10, 15 """
    def test5_set1(self):
        self.assertAlmostEqual(calculate_order(10, 10, 15), 6.55, places=4)

    """Tests operation with user input 10, 10, 20 """
    def test6_set1(self):
        self.assertAlmostEqual(calculate_order(10, 10, 20), 6.55, places=4)


if __name__ == '__main__':
    unittest.main()
