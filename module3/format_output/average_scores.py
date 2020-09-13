"""
Program: average_scores.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to get a student's first and
last names, their age, and three scores as input, then output
the mame, age, and average score.
"""


def average():
    score1 = input('first score: ')
    score2 = input('second score: ')
    score3 = input('third score: ')
    return (float(score1) + float(score2) + float(score3))/3.0


def main():
    first_name = input('Student\'s first name: ')
    last_name = input('Student\'s last name: ')
    age = input('Student\'s age: ')
    average_scores = average()
    print(last_name + ', ' + first_name + ': age ' + age, end=',')
    print(' average grade: {0:.2f}'.format(average_scores))


if __name__ == '__main__':
    main()


# Student's first name: Jay
# Student's last name: Luck
# Student's age: 14
# first score: 95
# second score: 81
# third score: 77
# Luck, Jay: age 14, average grade: 84.33
