"""
Program: test_basic_list_exception.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to contain
unit tests for basic_list_exception.py.
"""

import unittest
from unittest.mock import patch
import module7.fun_with_collections.basic_list as topic1


class TestList(unittest.TestCase):
    @patch('module7.fun_with_collections', return_value='7')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [7, 7, 7])

    @patch('fun_with_collections.topic1.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            topic1.make_list()  # call the function!

    @patch('fun_with_collections.topic1.get_input', return_value='-8')  # patch function for input
    def test_make_list_below_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            topic1.make_list()  # call the function!

    @patch('fun_with_collections.topic1.get_input', return_value='77')  # patch function for input
    def test_make_list_above_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            topic1.make_list()  # call the function!


if __name__ == '__main__':
    unittest.main()
