"""
Program: return_function.py
Author: Rachael Wolf
Last date modified: 10/03/2020

The purpose of this program is to explore functions and their creation.
It is an updated version of basic_function.py
"""


def is_convertible_to_float(value):
    """Tests whether a value is convertible to a float"""
    try:
        float(value)
        return True
    except:
        return False


def weekly_pay(hours_worked, hourly_pay_rate):
    """Prompts the user for name (string), hours worked (int), and
    hourly pay rate (float) and prints a message"""
    pass


def hourly_employee_input():
    """Prompts the user for name (string), hours worked (int), and
    hourly pay rate (float) and prints a message"""
    hours_check = False
    rate_check = False
    name = input('please enter your name: ')
    hours = input('please enter your hours worked (round to the nearest hour): ')
    while not hours_check:
        if not hours.isdigit():
            print('that is not a valid input. hours worked must be a positive integer')
            hours = input('please enter your hours worked (round to the nearest hour): ')
        elif int(hours) <= 0:
            print('that is not a valid input. hours worked must be positive')
            hours = input('please enter your hours worked (round to the nearest hour): ')
        else:
            hours_check = True
    rate = input('please enter your hourly pay rate as a decimal: ')
    while not rate_check:
        if not is_convertible_to_float(rate):
            print('that is not a valid input. pay rate must be a floating-point number')
            rate = input('please enter your hourly pay rate as a decimal: ')
        elif float(rate) <= 0:
            print('that is not a valid input. pay rate must be positive')
            rate = input('please enter your hourly pay rate as a decimal: ')
        else:
            rate_check = True
    print(name + ' receives a weekly pay of ' + weekly_pay(hours, rate))


def main():
    hourly_employee_input()


if __name__ == '__main__':
    main()
