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
    """Tests operation with user input price = 8, cash_coupon = 5, percent_coupon = 10
    Shipping will be $5.95, tax is 6%"""
    def test1_set1(self):
        self.assertAlmostEqual(calculate_order(8, 5, 10), 9.13, places=4)

    """Tests operation with user input 8, 5, 15"""
    def test2_set1(self):
        self.assertAlmostEqual(calculate_order(8, 5, 15), 8.98, places=4)

    """Tests operation with user input 8, 5, 20 """
    def test3_set1(self):
        self.assertAlmostEqual(calculate_order(8, 5, 20), 8.83, places=4)

    """Tests operation with user input 8, 10, 10 """
    def test4_set1(self):
        self.assertAlmostEqual(calculate_order(8, 10, 10), 6.43, places=4)

    """Tests operation with user input 8, 10, 15 """
    def test5_set1(self):
        self.assertAlmostEqual(calculate_order(8, 10, 15), 6.43, places=4)

    """Tests operation with user input 8, 10, 20 """
    def test6_set1(self):
        self.assertAlmostEqual(calculate_order(8, 10, 20), 6.43, places=4)

    """Tests operation with user input price = 20, cash_coupon = 5, percent_coupon = 10
    Shipping will be $7.95, tax is 6%"""
    def test1_set2(self):
        self.assertAlmostEqual(calculate_order(20, 5, 10), 22.65, places=4)

    """Tests operation with user input 20, 5, 15"""
    def test2_set2(self):
        self.assertAlmostEqual(calculate_order(20, 5, 15), 21.90, places=4)

    """Tests operation with user input 20, 5, 20 """
    def test3_set2(self):
        self.assertAlmostEqual(calculate_order(20, 5, 20), 21.15, places=4)

    """Tests operation with user input 20, 10, 10 """
    def test4_set2(self):
        self.assertAlmostEqual(calculate_order(20, 10, 10), 18.15, places=4)

    """Tests operation with user input 20, 10, 15 """
    def test5_set2(self):
        self.assertAlmostEqual(calculate_order(20, 10, 15), 17.65, places=4)

    """Tests operation with user input 20, 10, 20 """
    def test6_set2(self):
        self.assertAlmostEqual(calculate_order(20, 10, 20), 17.15, places=4)


if __name__ == '__main__':
    unittest.main()
