"""
Program: input_while_exit.py
Author: Rachael Wolf
Last date modified: 09/27/2020

The purpose of this program is to prompt the user for numeric input
between 1 and 100. Prompt the user until the input is in the correct
range. Once all the input is correct, store the input in a list.
This is an improved version using loop exit methods.
"""

storage = []
go_on = True
new_value = input('Please enter an integer from 1 to 100 or -1 to stop ')
while go_on:
    while not (1 <= int(new_value) <= 100):
        if int(new_value) == -1:
            print('Thank you for filling the list')
            break
        print('That is not a valid input')
        new_value = input('Please enter an integer from 1 to 100 or -1 to stop ')
    if 1 <= int(new_value) <= 100:
        storage.append(new_value)
        new_value = input('Please enter an integer from 1 to 100 or -1 to stop ')
    else:
        go_on = False

# print the list using a for loop
for i in storage:
    print(i)

# Please enter an integer from 1 to 100 or -1 to stop 45
# Please enter an integer from 1 to 100 or -1 to stop 773
# That is not a valid input
# Please enter an integer from 1 to 100 or -1 to stop 73
# Please enter an integer from 1 to 100 or -1 to stop -2
# That is not a valid input
# Please enter an integer from 1 to 100 or -1 to stop 24
# Please enter an integer from 1 to 100 or -1 to stop 8
# Please enter an integer from 1 to 100 or -1 to stop -1
# Thank you for filling the list
# 45
# 73
# 24
# 8


