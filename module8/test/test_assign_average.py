"""
Program: test_dict_membership.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain
unit tests for dict_membership.py.
"""

import unittest
import module8.more_fun_with_collections.dict_membership as topic1


class TestList(unittest.TestCase):
    def test_switch_average_A(self):
        self.assertEqual(100 >= topic1.in_dict('A') >= 90, True)

    def test_switch_average_B(self):
        self.assertEqual(90 > topic1.in_dict('B') >= 80, True)

    def test_switch_average_C(self):
        self.assertEqual(80 > topic1.in_dict('C') >= 70, True)

    def test_switch_average_D(self):
        self.assertEqual(70 > topic1.in_dict('D') >= 50, True)

    def test_switch_average_F(self):
        self.assertEqual(50 > topic1.in_dict('F'), True)

    def test_switch_average_non_key(self):
        self.assertRaises(topic1.in_dict('G'), ValueError)


if __name__ == '__main__':
    unittest.main()
