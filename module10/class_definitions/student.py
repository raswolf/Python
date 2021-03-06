"""
Program: student.py
Author: Rachael Wolf
Last date modified: 11/1/2020

This program contains a Class called Student and a function relating to it
The function included is: __str__()
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        def is_convertible_to_float(value):
            """Tests whether a value is convertible to a float"""
            try:
                float(value)
                return True
            except:
                return False
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)
                and name_characters.issuperset(major) and is_convertible_to_float(gpa)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
