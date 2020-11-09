"""
Program: student.py
Author: Rachael Wolf
Last date modified: 11/8/2020

This program contains a Class called Student and functions relating to it
The functions overridden are: __str__() and display()
The functions added are change_major() and update_gpa()
"""
import module11.class_definitions.person as p


def is_convertible_to_float(value):
    """Tests whether a value is convertible to a float"""
    try:
        float(value)
        return True
    except:
        return False


class Student(p.Person):
    """Student class"""
    def __init__(self, student_id, fname, lname, major='Computer Science', gpa=0.0):
        super().__init__(fname, lname)
        if not is_convertible_to_float(gpa):
            raise ValueError
        if not isinstance(student_id, int):
            raise ValueError
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " \
               + self.major + " with gpa: " + str(self.gpa)

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        if not is_convertible_to_float(new_gpa):
            raise ValueError
        else:
            self.gpa = new_gpa

    def display(self):
        return self.last_name + ", " + self.first_name + ":(" + str(self.student_id) + ") " \
               + self.major + " gpa: " + str(self.gpa)


# driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
