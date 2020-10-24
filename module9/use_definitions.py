"""
Program: use_definitions.py
Author: Rachael Wolf
Last date modified: 10/24/2020

this program is a Python program that uses the module my_definitions
"""

import module9.my_definitions as defs


test_dict = {'A': 11, 'B': 3, 'C': 5, 'D': 19, 'E': 13, 'F': 23}
test_set = {11, 3, 5, 19, 13, 23}


def main():
    defs.message()
    name = input('Welcome.  Who are you? ')
    defs.greeting(name)
    defs.print_dict(test_dict)
    defs.print_set(test_set)


if __name__ == '__main__':
    main()
