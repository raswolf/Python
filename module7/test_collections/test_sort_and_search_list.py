"""
Program: test_sort_and_search_list.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to contain
unit tests for sort_and_search_list.py.
"""

import unittest
from module7.fun_with_collections.sort_and_search_list import search_list


class MyTestCase(unittest.TestCase):

    def test_search_list_found(self):
        self.assertEqual(search_list(2.1, [2.1, 3.4, 8.2]), 0)

    def test_search_list_not_found(self):
        self.assertEqual(search_list(5.5, [2.1, 3.4, 8.2]), -1)


if __name__ == '__main__':
    unittest.main()
