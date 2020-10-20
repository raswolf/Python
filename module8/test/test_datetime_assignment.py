"""
Program: test_datetime_assignment.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain
unit tests for datetime_assignment.py.
"""

import unittest
import datetime
import module8.more_fun_with_collections.datetime_assignment as topic1

my_birthday = datetime.datetime(2020, 5, 26)


class TestList(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(topic1.half_birthday(my_birthday), datetime.datetime(2020, 11, 25))


if __name__ == '__main__':
    unittest.main()
