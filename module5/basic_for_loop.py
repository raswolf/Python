"""
Program: basic_for_loop.py
Author: Rachael Wolf
Last date modified: 09/27/2020

The purpose of this program is to Declare a list of floating point numbers,
Write a for loop to print each, and Write a second for loop to print
the odd number descending from 99 to 33 (including 99 and 33)
"""

numberlist = [5.8, 3.37, 12.09, 6.55, 7.0, 18.49]

for v in numberlist:
    print(v, end=' ')
print()

for z in range(99, 32, -2):
    if z == 67:
        print(z)
    else:
        print(z, end=' ')
