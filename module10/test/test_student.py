"""
Program: test_student.py
Author: Rachael Wolf
Last date modified: 11/02/2020

The purpose of this program is to contain
unit tests for student.py.
"""

import unittest
import module10.class_definitions.student as sdt


class TestList(unittest.TestCase):
    def setUp(self):
        self.student = sdt.Student('Luck', 'Jay', 'Horticulture')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Luck')
        self.assertEqual(self.student.first_name, 'Jay')
        self.assertEqual(self.student.major, 'Horticulture')

    def test_object_created_all_attributes(self):
        self.assertTrue(False)

    def test_student_str(self):
        student1 = sdt.Student('Lisa', 'Briggs', 'Political Science', 3.28)
        assert student1.last_name == 'Lisa'
        assert student1.first_name == 'Briggs'
        assert student1.major == 'Political Science'
        assert student1.gpa == 3.28

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