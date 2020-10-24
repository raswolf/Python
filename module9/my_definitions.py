"""
Program: my_definitions.py
Author: Rachael Wolf
Last date modified: 10/24/2020

this program is a Python module that includes the following:
A function greeting that prints a friendly greeting
A function message that prints you as the author of the code
A function print_dict that accepts a dictionary and prints the pairs (key, value) one per line
A function print_set that accepts a set and prints the set one item per line
"""


def greeting(name):
    print('Hello, ' + name)


def message():
    print('This code was written by Rachael Wolf')


def print_dict(dictionary_to_print):
    for n in dictionary_to_print:
        print(n + ': ' + str(dictionary_to_print[n]))


def print_set(set_to_print):
    for n in set_to_print:
        print(n)
