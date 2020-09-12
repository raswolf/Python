"""
Program: string_methods.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to explore
the methods in python associated with strings.
"""

movie_role = 'someone in something (decisions are hard)'

# part 1
print(movie_role.capitalize())
print(movie_role.find('eth'))

# part 2
print(movie_role.index('one'))
print(movie_role.isalnum())

# part 3
print(movie_role.isalpha())
print(movie_role.isdigit())

# part 4
print(movie_role.islower())
print(movie_role.isupper())

# part 5
print(movie_role.isspace())
print(movie_role.startswith('not'))
