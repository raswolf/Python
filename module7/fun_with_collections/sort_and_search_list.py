"""
Program: sort_and_search_list.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to
"""

import module7.fun_with_collections.basic_list


def sort_list(a_list):
    """sorts a list.  Does not return, because it alters the list used as input"""
    a_list.sort()


def search_list(item, a_list):
    """searches a list for a specified item and returns the index of that item
    :return the index of the search item, or -1 if the item is not in the list"""
    for n in a_list:
        if n == item:
            return a_list.index(n)
    return -1
