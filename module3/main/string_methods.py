"""
Program: string_methods.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to explore
the methods in python associated with strings.
"""

movie_role = 'Westley from The Princess Bride'


def main():
    index = input('Which set to run? (1-5)')
    if index == '1':
        print('capitalize: ' + movie_role.capitalize())
        print('find "ss": ' + str(movie_role.find('ss')))
    if index == '2':
        print('index "ley": ' + str(movie_role.index('ley')))
        print('isalnum: ' + str(movie_role.isalnum()))
    if index == '3':
        print('isalpha: ' + str(movie_role.isalpha()))
        print('isdigit: ' + str(movie_role.isdigit()))
    if index == '4':
        print('islower: ' + str(movie_role.islower()))
        print('isupper: ' + str(movie_role.isupper()))
    if index == '5':
        print('isspace: ' + str(movie_role.isspace()))
        print('startswith "not": ' + str(movie_role.startswith('not')))


if __name__ == '__main__':
    main()
