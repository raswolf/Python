"""
Program: compound_expression.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to investigate complex expressions.
"""

MIN = 0
MAX = 10


def main():
    y = input('enter a number y for tests: ')
    y = int(y)
    print("y > MAX: " + str(y > MAX))
    print("y < MIN: " + str(y < MIN))
    x = input('enter a number x for tests: ')
    x = int(x)
    print("MIN < x  < MAX: " + str(MIN < x < MAX))
    print("MIN <= x  < MAX: " + str(MIN <= x < MAX))
    print("MIN < x <= MAX: " + str(MIN < x <= MAX))


if __name__ == '__main__':
    main()
