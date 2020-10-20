"""
Program: test_dict_membership.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain
unit tests for dict_membership.py.
"""

import unittest
import module8.more_fun_with_collections.assign_average as topic1


class TestList(unittest.TestCase):
    def test_switch_average_A(self):
        self.assertTrue(100 >= int(topic1.switch_average('A')) >= 90)

    def test_switch_average_B(self):
        self.assertTrue(90 > int(topic1.switch_average('B')) >= 80)

    def test_switch_average_C(self):
        self.assertTrue(80 > int(topic1.switch_average('C')) >= 70)

    def test_switch_average_D(self):
        self.assertTrue(70 > int(topic1.switch_average('D')) >= 50)

    def test_switch_average_F(self):
        self.assertTrue(50 > int(topic1.switch_average('F')) >= 0)

    def test_switch_average_non_key(self):
        self.assertEqual(topic1.switch_average('G'), 'Invalid Grade')


if __name__ == '__main__':
    unittest.main()
