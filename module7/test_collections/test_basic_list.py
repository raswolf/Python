"""
Program: test_basic_list.py
Author: Rachael Wolf
Last date modified: 10/11/2020

The purpose of this program is to contain
unit tests for basic_list.py.
"""

import unittest
from unittest.mock import patch
import module7.fun_with_collections.basic_list as topic1


class TestList(unittest.TestCase):
    @patch('module7.fun_with_collections', return_value='7')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [7, 7, 7])


if __name__ == '__main__':
    unittest.main()