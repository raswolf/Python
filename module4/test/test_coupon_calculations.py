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
    """Tests operation with user input price = 40, cash_coupon = 5, percent_coupon = 20"""
    def test1_calculate(self):
        self.assertAlmostEqual(calculate_order(40, 5, 20), 28, places=4)

    """Tests operation with user input 50, 0, 15"""
    def test2_calculate(self):
        self.assertAlmostEqual(calculate_order(50, 0, 15), 42.5, places=4)

    """Tests operation with user input 15, 20, 10 (no instructions were given to prevent this)"""
    def test3_super_cash(self):
        self.assertAlmostEqual(calculate_order(15, 20, 10), -0.5, places=4)

    """Tests operation with user input 40, 5, 110 (no instructions were given to prevent this)"""
    def test4_super_percent(self):
        self.assertAlmostEqual(calculate_order(40, 5, 110), -3.5, places=4)


if __name__ == '__main__':
    unittest.main()
