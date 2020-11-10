"""
Program: person.py
Author: Rachael Wolf
Last date modified: 11/8/2020

This program contains a Class called Address and another called Person, which uses Address
"""


class Address:
    """Address class for US addresses"""
    def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '-")
        num_characters = set("1234567890 -()")
        if not (name_characters.issuperset(st_name) and name_characters.issuperset(st_type)
                and name_characters.issuperset(city) and name_characters.issuperset(state)):
            raise ValueError
        if not (num_characters.issuperset(str(st_number)) and num_characters.issuperset(str(zip))):
            raise ValueError
        self.street_number = str(st_number)
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zip

    def __str__(self):
        return self.street_number + ' ' + self.street_name + '\n' + self.city + ', ' + self.state

    def display(self):
        return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
               + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=None):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if (addy is not None) and (not isinstance(addy, Address)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        if self.address is None:
            return str(self.last_name) + ", " + str(self.first_name)
        else:
            return str(self.last_name) + ", " + str(self.first_name) + '\n' + str(self.address)
