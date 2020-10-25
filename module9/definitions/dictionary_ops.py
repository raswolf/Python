"""
Program: dictionary_ops.py
Author: Rachael Wolf
Last date modified: 10/25/2020

this program is a Python module that includes the following:
A function print_dict that accepts a dictionary and prints the pairs (key, value) one per line
"""


def print_dict(dictionary_to_print):
    """accepts a dictionary and prints the pairs (in the form 'key: value') one per line"""
    for n in dictionary_to_print:
        print(n + ': ' + str(dictionary_to_print[n]))
