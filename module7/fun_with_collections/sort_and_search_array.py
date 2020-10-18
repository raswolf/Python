"""
Program: sort_and_search_array.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to
"""


def sort_array(a_array):
    """ will sort the array. Does not return, because it alters the array used as input"""
    a_list = a_array.to_list()
    a_list.sort
    return a_list
    

def search_array(item, a_array):
    """returns the index of the object in the list or a -1 if the item is not found
    :return the index of the search item, or -1 if the item is not in the array"""
    for n in a_array:
        if n == item:
            return a_array.index(n)
    return -1


