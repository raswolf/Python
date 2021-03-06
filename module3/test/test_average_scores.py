"""
Program: test_average_scores.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to contain
unit tests for average_scores.py.
"""

import unittest
from module3.format_output.average_scores import average


class FunctionTestCase(unittest.TestCase):
    """Tests operation with user input 70, 82, 67"""
    def test1_average(self):
        self.assertEqual(average(), 73)

    """Tests operation with user input 95, 81, 77"""
    def test2_average(self):
        self.assertEqual(average(), 84.33)


if __name__ == '__main__':
    unittest.main()
