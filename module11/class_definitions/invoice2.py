"""
Program: invoice2.py
Author: Rachael Wolf
Last date modified: 11/8/2020

This program contains a Class called Invoice and some functions relating to it
The functions included are: add_item(), create_invoice(), display(), str(), and repr()
"""
import module10.class_definitions.customer as c


class Invoice:
    """A class representing an invoice, with an invoice ID, a Customer object, and a
    dictionary of item names and prices"""

    def __init__(self, invoice_id, customer, items_with_price=None):

        if items_with_price is None:
            self.items_with_price = {'none': 0.00}
        else:
            self.items_with_price = items_with_price
        if isinstance(customer, c.Customer):
            self.customer = customer
        else:
            raise AttributeError('AttributeError: \'Invoice\' object has no attribute \'customer\'')
        if isinstance(invoice_id, int):
            self.invoice_id = int(invoice_id)
        else:
            raise AttributeError('AttributeError: \'Invoice\' object has no attribute \'iid\'')

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
        price = 0.0
        for k in self.items_with_price:
            price += self.items_with_price[k]
            print(str(k) + ': ' + str(self.items_with_price[k]))
        tax = price * tax
        print('Tax: {0:.2f}'.format(tax))
        print('Total: {0:.2f}'.format(price + tax))

    def display(self):
        """returns a more comprehensive string of the Invoice object"""
        full_name = str(self.customer.first_name) + " " + str(self.customer.last_name)
        return (str(self.customer.customer_id) + "\n" + full_name + "\n" + str(self.customer.address) + "\n" +
               self.customer.phone_number)

    def str(self):
        """returns a string of the Invoice object. same as repr()"""
        i_string = self.customer.first_name + ' ' + self.customer.last_name + ', ' + self.customer.phone_number
        return i_string

    def repr(self):
        """returns a string of the Invoice object. same as str()"""
        i_string = self.customer.first_name + ' ' + self.customer.last_name + ', ' + self.customer.phone_number
        return i_string


# Drive
captain_mal = c.Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item('iPad', 799.99)
invoice.add_item('Surface', 999.99)
print()
invoice.create_invoice(.07)
del captain_mal
del invoice
