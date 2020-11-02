"""
Program: test_student.py
Author: Rachael Wolf
Last date modified: 11/02/2020

The purpose of this program is to contain
unit tests for student.py.
"""

import unittest
import module10.class_definitions.student as topic1


class TestList(unittest.TestCase):
    def test_object_created_required_attributes(self):
        self.assertTrue(False)

    def test_object_created_all_attributes(self):
        self.assertTrue(False)

    def test_student_str(self):
        self.assertTrue(False)

    def test_object_not_created_error_last_name(self):
        self.assertTrue(False)

    def test_object_not_created_error_first_name(self):
        self.assertTrue(False)

    def test_object_not_created_error_major(self):
        self.assertTrue(False)

    def test_object_not_created_error_gpa(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()