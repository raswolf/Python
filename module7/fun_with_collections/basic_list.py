"""
Program: basic_list.py
Author: Rachael Wolf
Last date modified: 10/11/2020

The purpose of this program is to
"""


def make_list():
    """Asks for 3 user inputs and stores them in a list
    :returns a list of the user inputs"""
    itemlist = []
    for x in range(0, 3):
        item = get_input()
        itemlist.append(int(item))
    return itemlist


def get_input():
    item = input('Please enter a number: ')
    return item

