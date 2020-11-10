"""
Program: employee2.py
Author: Rachael Wolf
Last date modified: 11/9/2020

This program contains a Class called Employee and some functions relating to it
The functions included are: set_last_name(), set_first_name(), display(), str(), and repr()
"""
import my_stuff.my_tools as t
import datetime


class Employee:
    """A class representing an employee, with a first and last name, contact information, and employment information"""
    def __init__(self, name, surname, address, phone_number):
        self.first_name = name
        self.last_name = surname
        self.address = address
        self.phone_number = phone_number

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
        return full_name + "\n" + str(self.address)

    def str(self):
        """returns a string of the Employee object.  same as repr()"""
        e_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return e_string

    def repr(self):
        """returns a string of the Employee object. same as str()"""
        e_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return e_string


class SalariedEmployee(Employee):
    def __init__(self, name, surname, address, phone_number, start_date, salary):
        super().__init__(name, surname, address, phone_number)
        if not t.is_convertible_to_float(salary):
            raise ValueError
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, new_salary):
        if not t.is_convertible_to_float(new_salary) or (new_salary < self.salary):
            raise ValueError
        else:
            self.salary = new_salary

    def display(self):
        """returns a more comprehensive string of the SalariedEmployee object"""
        full_name = str(self.first_name) + " " + str(self.last_name)
        salary_line = "Salaried employee: $" + str(self.salary) + "/year "
        return full_name + "\n" + str(self.address) + "\n" + salary_line + "Start date: " + str(self.start_date)


class HourlyEmployee(Employee):
    def __init__(self, name, surname, address, phone_number, start_date, hourly_pay):
        super().__init__(name, surname, address, phone_number)
        if not t.is_convertible_to_float(hourly_pay):
            raise ValueError
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    def give_raise(self, new_pay):
        if not t.is_convertible_to_float(new_pay) or (new_pay < self.hourly_pay):
            raise ValueError
        else:
            self.hourly_pay = new_pay

    def display(self):
        """returns a more comprehensive string of the HourlyEmployee object"""
        full_name = str(self.first_name) + " " + str(self.last_name)
        pay_line = "Hourly employee: $" + str(self.hourly_pay) + "/hour "
        return full_name + "\n" + str(self.address) + "\n" + pay_line + "Start date: " + str(self.start_date)


# Drive
me_salaried = SalariedEmployee('Rachael', 'Wolf', '555 Auburn Rd \n Fake, IA', '(319)-382-3100',
                               datetime.date.today(), 40000)
print(me_salaried.display())
me_salaried.give_raise(45000)
print(me_salaried.display())
del me_salaried

print()

me_hourly = HourlyEmployee('Rachael', 'Wolf', '555 Auburn Rd \n Fake, IA', '(319)-382-3100',
                           datetime.date.today(), 10.00)
print(me_hourly.display())
me_hourly.give_raise(12.00)
print(me_hourly.display())
del me_hourly
