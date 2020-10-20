"""
Program: assign_average.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain a function switch_average.
In the instructions, it is not clear to me exactly what this function is supposed to do
I am writing my code under the assumption I am meant to decide exactly what the different
cases are meant to be and what should be done in each case.
This program produces random test scores, as strings convertible to integers, which are within
the range indicated by the user-provided letter grade.
"""

import random


def get_A():
    score = random.randrange(90, 101)
    return str(score)


def get_B():
    score = random.randrange(80, 90)
    return str(score)


def get_C():
    score = random.randrange(70, 80)
    return str(score)


def get_D():
    score = random.randrange(50, 70)
    return str(score)


def get_F():
    score = random.randrange(0, 50)
    return str(score)


def switch_average(score_key):
    """Takes a letter grade and returns a corresponding number grade
    :param score_key a letter grade A, B, C, D, or F
    :returns a string denoting a score that would receive the provided grade"""
    switcher = {'A': get_A,
                'B': get_B,
                'C': get_C,
                'D': get_D,
                'F': get_F}
    func = switcher.get(score_key, lambda: "Invalid Grade")
    return func()
