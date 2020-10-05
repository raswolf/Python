"""
Program: inner_functions_assignment.py
Author: Rachael Wolf
Last date modified: 10/03/2020

The purpose of this program is to.
"""


def measurements(m_list):
    """Takes the length and width of a rectangle and describes the perimeter and area
    :param m_list, a list containing the side measurements of the rectangle
    :returns a string describing the perimeter and area of the specified rectangle"""
    def area(a_list):
        return float(a_list[0]) * float(a_list[1])

    def perimeter(a_list):
        return (float(a_list[0]) + float(a_list[1])) * 2

    description = 'Perimeter = ' + str(perimeter(m_list)) + ' Area = ' + str(area(m_list))
    return description

