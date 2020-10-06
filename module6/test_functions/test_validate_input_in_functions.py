"""
Program: test_validate_input_in_functions.py
Author: Rachael Wolf
Last date modified: 10/05/2020

The purpose of this program is to contain
unit tests for validate_input_in_functions.py.
"""

import unittest
from module6.more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):

    def test_score_input_test_name(self):
        """checking that the function works with only the mandatory argument"""
        self.assertEqual(score_input('Maggie'), 'Maggie: 0')

    def test_score_input_test_score_valid(self):
        """checking that the function works with the mandatory argument and the score option:
        one good input"""
        self.assertEqual(score_input('Maggie', 56), 'Maggie: 56')

    def test_score_input_test_score_below_range(self):
        """checking that the function works with the mandatory argument and the score option"""
        self.assertEqual(score_input('Maggie', -56), 'Invalid test score, try again!')

    def test_score_input_test_score_above_range(self):
        """checking that the function works with the mandatory argument and the score option:"""
        self.assertEqual(score_input('Maggie', 156), 'Invalid test score, try again!')

    def test_score_input_test_score_non_numeric(self):
        """checking that the function does not work with a non-numeric score option"""
        with self.assertRaises(ValueError):
            score_input('Maggie', 'what')

    def test_score_input_invalid_message(self):
        """checking that the function works with the mandatory argument and the score option:"""
        self.assertEqual(score_input('Maggie', 56, 'invalid'), 'Maggie: 56')


if __name__ == '__main__':
    unittest.main()
