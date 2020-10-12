"""
Program: param_function.py
Author: Rachael Wolf
Last date modified: 10/03/2020

The purpose of this program is to explore functions and parameters.
"""


def multiply_string(message, n):
    """Takes a string message and a number n and returns the string with message printed n times"""
    return message * n


def main():
    print('message = Python')
    print('repeats = 5')
    print(multiply_string('Python', 5))


if __name__ == '__main__':
    main()
