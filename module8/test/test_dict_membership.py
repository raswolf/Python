"""
Program: test_dict_membership.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain
unit tests for dict_membership.py.
"""

import unittest
import module8.more_fun_with_collections.dict_membership as topic1

test_dict = {'A': 11, 'B': 3, 'C': 5, 'D': 19, 'E': 13, 'F': 23}


class TestList(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(topic1.in_dict(test_dict, 3), True)

    def test_in_set_false(self):
        self.assertEqual(topic1.in_dict(test_dict, 4), False)


if __name__ == '__main__':
    unittest.main()
