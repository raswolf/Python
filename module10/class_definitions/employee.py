"""
Program: employee.py
Author: Rachael Wolf
Last date modified: 11/1/2020

This program contains a Class called Employee and some functions relating to it
The functions included are: set_last_name(), set_first_name(), display(), str(), and repr()
"""
import datetime


class Employee:
    """A class representing an employee, with a first and last name, contact information, and employment information"""

    def __init__(self, name, surname, address, phone_number, salaried, start_date, salary):

        self.first_name = name
        self.last_name = surname
        self.address = address
        self.phone_number = phone_number
        self.salaried = bool(salaried)
        self.start_date = start_date
        self.salary = salary

    def set_last_name(self, surname):
        """sets or alters the last_name string of the Employee object
        :param surname the last name of the Employee"""
        self.last_name = surname

    def set_first_name(self, name):
        """sets or alters the first_name string of the Employee object
        :param name the first name of the Employee"""
        self.first_name = name

    def display(self):
        """returns a more comprehensive string of the Employee object"""
        full_name = str(self.first_name) + " " + str(self.last_name)
        salary_line = ''
        if self.salaried:
            salary_line = "Salaried employee: $" + str(self.salary) + "/year"
        else:
            salary_line = "Hourly employee: $" + str(self.salary) + "/hour"
        return full_name + "\n" + str(self.address) + "\n" + salary_line + "Start date: " + str(self.start_date)

    def str(self):
        """returns a string of the Employee object.  same as repr()"""
        e_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return e_string

    def repr(self):
        """returns a string of the Employee object. same as str()"""
        e_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return e_string


# Drive
emp = Employee('Matthew', 'Ruiz', '519 Grant St \nEllis, New Jersey', '(614) 544 9823', True,
               datetime.date.today(), 40000)   # call the constructor
emp.set_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
del emp
