"""
Program: my_definitions.py
Author: Rachael Wolf
Last date modified: 10/24/2020

this program is a Python module that includes the following:
A function greeting that prints a friendly greeting
A function message that prints me as the author of the code
A function print_dict that accepts a dictionary and prints the pairs (key, value) one per line
A function print_set that accepts a set and prints the set one item per line
"""


def greeting(name):
    """prints a friendly greeting addressed to the person whose name is used as input"""
    print('Hello, ' + name)


def message():
    """prints a message crediting me as the author of the code"""
    print('This code was written by Rachael Wolf')


def print_dict(dictionary_to_print):
    """accepts a dictionary and prints the pairs (in the form 'key: value') one per line"""
    for n in dictionary_to_print:
        print(n + ': ' + str(dictionary_to_print[n]))


def print_set(set_to_print):
    """accepts a set and prints the set elements one item per line"""
    for n in set_to_print:
        print(n)
