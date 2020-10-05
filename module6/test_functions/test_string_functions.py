"""
Program: test_string_functions.py
Author: Rachael Wolf
Last date modified: 10/4/2020

The purpose of this program is to contain
unit tests for string_functions.py.
"""

import unittest
from module6.more_functions.string_functions import multiply_string


class FunctionTestCase(unittest.TestCase):
    """Tests operation with parameters 'Rachael' and 7"""
    def test1_set1(self):
        self.assertEqual(multiply_string('Rachael', 7), 'RachaelRachaelRachaelRachaelRachaelRachaelRachael')


if __name__ == '__main__':
    unittest.main()
