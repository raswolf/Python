"""
Program: student.py
Author: Rachael Wolf
Last date modified: 11/8/2020

This program contains a Class called Student and a function relating to it
The functions included are: __str__(), change_major(), update_gpa() and display()
"""
import module11.class_definitions.Person as p


def is_convertible_to_float(value):
    """Tests whether a value is convertible to a float"""
    try:
        float(value)
        return True
    except:
        return False


class Student:
    """Student class"""
    def __init__(self, person, major, gpa=0.0):

        if not isinstance(person, p.Person):
            raise ValueError
        if not is_convertible_to_float(gpa):
            raise ValueError
        self.person = person
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.person.last_name + ", " + self.person.first_name + " has major " \
               + self.major + " with gpa: " + str(self.gpa)

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        if not is_convertible_to_float(new_gpa):
            raise ValueError
        else:
            self.gpa = new_gpa

    def display(self):
        return self.person.last_name + ", " + self.person.first_name + " has major " \
               + self.major + " with gpa: " + str(self.gpa)


# driver
me = p.Person("Wolf", "Rachael")
student_me = Student(me, "Computer Science", 4.0)
print(student_me.display())
student_me.change_major("Being Awesome!")
student_me.update_gpa(3.0)
print(student_me.display())
del student_me
del me

