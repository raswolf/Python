"""
Program: manager.py
Author: Rachael Wolf
Last date modified: 11/9/2020

This program contains a Class called Manager which inherits from Person and Employee
It seems to me it would make more sense to have Employee be a subclass of Person.
"""
import module11.class_definitions.person as p
import module11.class_definitions.employee2 as e
import datetime


class Manager(p.Person, e.SalariedEmployee):
    """Manager class which inherits from Person and Employee"""
    def __init__(self, name, surname, address, phone_number, start_date, salary, department, direct_reports=None):
        super().__init__(name, surname, address)
        e.SalariedEmployee.__init__(self, self.first_name, self.last_name, str(self.address), phone_number, start_date,
                                    salary)
        if direct_reports is None:
            direct_reports = []
        self.department = department
        self.direct_reports = direct_reports


# driver
me_manager = Manager('Rachael', 'Wolf', p.Address(555, "Auburn", "Rd", "Fake", "IA", "50014"), '(319)-382-3100',
                     datetime.date.today(), 40000, "Python")
# uses display() from Person
print(me_manager.display())
print(str(me_manager.direct_reports))
me_manager.give_raise(42000)
print(me_manager.display())
del me_manager
