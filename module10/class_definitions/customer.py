"""
Program: customer.py
Author: Rachael Wolf
Last date modified: 11/1/2020

This program contains a Class called Customer and some functions relating to it
The functions included are: set_last_name(), set_first_name(), display(), str(), and repr()
"""


class Customer:
    """A class representing a customer, with a customer ID, first and last name, and contact information"""

    def __init__(self, customer_id, name, surname, phone_number, address):

        if isinstance(self.customer_id, int):
            self.customer_id = int(customer_id)
        else:
            raise AttributeError('AttributeError: \'Customer\' object has no attribute \'cid\'')
        self.first_name = name
        self.last_name = surname
        self.address = address
        self.phone_number = phone_number

    def set_last_name(self, surname):
        """sets or alters the last_name string of the Customer object
        :param surname the last name of the Customer"""
        self.last_name = surname

    def set_first_name(self, name):
        """sets or alters the first_name string of the Customer object
        :param name the first name of the Customer"""
        self.first_name = name

    def display(self):
        """returns a more comprehensive string of the Customer object"""
        full_name = str(self.first_name) + " " + str(self.last_name)
        return str(self.customer_id) + "\n" + full_name + "\n" + str(self.address) + "\n" + self.phone_number

    def str(self):
        """returns a string of the Customer object. same as repr()"""
        e_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return e_string

    def repr(self):
        """returns a string of the Customer object.  same as str()"""
        e_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return e_string


# Drive
customer1 = Customer(25543, 'Matthew', 'Ruiz', '(614) 544 9823',
                     '519 Grant St \nEllis, New Jersey')   # call the constructor
print(customer1.display())  # display returns a str, so print the information
customer2 = Customer('goose', 'Laura', 'Maduro', '(822) 282 5743'
                     '114 Coral Ave \n Hark, New Jersey')
print(customer2.display())  # display returns a str, so print the information
del customer1
del customer2
