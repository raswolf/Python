"""
Program: string_methods.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to explore
the methods in python associated with strings.
"""

movie_role = 'Westley from The Princess Bride'


def set_1():
    print('capitalize: ' + movie_role.capitalize())
    print('find: ' + str(movie_role.find('ss')))


def set_2():
    print('index: ' + str(movie_role.index('ley')))
    print('isalnum: ' + str(movie_role.isalnum()))


def set_3():
    print('isalpha: ' + str(movie_role.isalpha()))
    print('isdigit: ' + str(movie_role.isdigit()))


def set_4():
    print('islower: ' + str(movie_role.islower()))
    print('isupper: ' + str(movie_role.isupper()))


def set_5():
    print('isspace: ' + str(movie_role.isspace()))
    print('startswith: ' + str(movie_role.startswith('not')))


def main():
    index = input('Which set to run? (1-5)')
    if index == 1:
        set_1()
    if index == 2:
        set_2()
    if index == 3:
        set_3()
    if index == 4:
        set_4()
    if index == 5:
        set_5()


if __name__ == '__main__':
    main()
