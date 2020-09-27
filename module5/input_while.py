"""
Program: input_while.py
Author: Rachael Wolf
Last date modified: 09/27/2020

The purpose of this program is to prompt the user for numeric input
between 1 and 100. Prompt the user until the input is in the correct
range. Once all the input is correct, store the input in a list.
"""

storage = []
go_on = True
new_value = input('Please enter an integer from 1 to 100 or 0 to stop ')
while go_on:
    # while sentinel value is not stopping value
    while not (0 <= int(new_value) <= 100):
        print('that is not a valid input')
        new_value = input('Please enter an integer from 1 to 100 or 0 to stop ')
    if int(new_value) == 0:
        go_on = False
        print('Thank you for filling the list')
    else:
        storage.append(new_value)
        new_value = input('Please enter an integer from 1 to 100 or 0 to stop ')

# print the list using a for loop
for i in storage:
    print(i)
