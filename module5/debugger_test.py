"""
Program: debugger_test.py
Author: Rachael Wolf
Last date modified: 09/28/2020

The purpose of this program is to practice using the debugger.
"""


def print_to_number(number):
    """Prints to the number value passed in, beginning at 1"""
    for counter in range(1, number + 1):
        print(counter)


def main():
    counter = input('What number should I count to? ')
    print_to_number(counter)


if __name__ == "__main__":
    print_to_number(5)

