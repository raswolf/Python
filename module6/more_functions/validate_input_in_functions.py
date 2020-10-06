"""
Program: validate_input_in_functions.py
Author: Rachael Wolf
Last date modified: 10/05/2020

The purpose of this program is to explore default values in function structuring.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """Takes a test_name, test_score, and invalid_message.  Validates the test_score,
    asks the user for a valid test score until it is in the range, then prints valid input as 'Test name: ##'.
    :param test_name mandatory.  The name of the test taker
    :param test_score optional, with default value of 0 (zero). should be between 0-100.
    :param invalid_message optional, with default value 'Invalid test score, try again!'
    :returns a string formatted as 'Test name: ##'"""

    # return { test_name: test_score} before the return statement for later use.
    return test_name + ': ' + str(test_score)
