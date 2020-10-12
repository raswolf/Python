"""
Program: basic_list.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to create a list of three items from user input
"""


def make_list():
    """Asks for 3 user inputs and stores them in a list
    :returns a list of the user inputs"""
    itemlist = []
    for x in range(0, 3):
        item = get_input()
        while not item.isdigit():
            print('that is not a valid input')
            item = get_input()
        itemlist.append(int(item))
    return itemlist


def get_input():
    item = input('Please enter a number: ')
    return item

