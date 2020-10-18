"""
Program: test_set_membership.py
Author: Rachael Wolf
Last date modified: 10/18/2020

The purpose of this program is to contain
unit tests for set_membership.py.
"""

import unittest
import module8.more_fun_with_collections.set_membership as topic1

test_set = {11, 3, 5, 19, 13, 23}


class TestList(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(topic1.in_set(test_set, 3), True)

    def test_in_set_false(self):
        self.assertEqual(topic1.in_set(test_set, 4), False)


if __name__ == '__main__':
    unittest.main()
