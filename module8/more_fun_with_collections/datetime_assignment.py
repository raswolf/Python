"""
Program: datetime_assignment.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to contain a function half_birthday() which calculates
a person's half-birthday based on their most recent birthday
"""

import datetime


def half_birthday(birthday):
    """Takes a letter grade and returns a corresponding number grade
    :param birthday the date of a person's most recent birthday
    :returns the date of that person's subsequent half-birthday"""
    next_date = birthday + datetime.timedelta(days=183)
    return next_date

