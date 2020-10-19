"""
Program: set_membership.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain a function in_set
which tests whether a particular element is in a given set
"""


def in_set(q_set, element):
    """accepts a set and return a boolean value stating if the element is in the set
    :returns True if the element is in the set, false otherwise"""
    for e in q_set:
        if e == element:
            return True
    return False

