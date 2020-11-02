"""
Program: invoice.py
Author: Rachael Wolf
Last date modified: 11/1/2020

This program contains a Class called Invoice and some functions relating to it
The functions included are: add_item(), create_invoice(), display(), str(), and repr()
"""


class Invoice:
    """A class representing an invoice, with an invoice ID, information regarding the customer, and a
    dictionary of item names and prices"""

    def __init__(self, invoice_id, customer_id, name, surname, phone_number, address, items_with_price=None):

        if items_with_price is None:
            self.items_with_price = {'none': 0.00}
        else:
            self.items_with_price = items_with_price
        if isinstance(self.customer_id, int):
            self.customer_id = int(customer_id)
        else:
            raise AttributeError('AttributeError: \'Invoice\' object has no attribute \'cid\'')
        if isinstance(self.invoice_id, int):
            self.invoice_id = int(invoice_id)
        else:
            raise AttributeError('AttributeError: \'Invoice\' object has no attribute \'iid\'')
        self.first_name = name
        self.last_name = surname
        self.address = address
        self.phone_number = phone_number

    def add_item(self, item_name, item_price):
        """adds an item to items_with_price dictionary
        :param item_name the name of the item being added
        :param item_price the price of the item being added"""
        if 'none' in self.items_with_price:
            self.items_with_price.clear()
        self.items_with_price.update({str(item_name): float(item_price)})

    def create_invoice(self, tax):
        """prints each item and price, then a total with tax calculated
        :param tax the tax rate to be used in calculation.  should be a decimal less than 1"""
        pass

    def display(self):
        """returns a more comprehensive string of the Invoice object"""
        full_name = str(self.first_name) + " " + str(self.last_name)
        return str(self.customer_id) + "\n" + full_name + "\n" + str(self.address) + "\n" + self.phone_number

    def str(self):
        """returns a string of the Invoice object. same as repr()"""
        i_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return i_string

    def repr(self):
        """returns a string of the Invoice object. same as str()"""
        i_string = self.first_name + ' ' + self.last_name + ', ' + self.phone_number
        return i_string


# Drive
