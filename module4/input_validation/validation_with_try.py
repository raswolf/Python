"""
Program: validation_with_try.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to get a student's first and
last names, their age, and three scores as input, then output
the mame, age, and average score.
"""


def average(score1, score2, score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError

    return (float(score1) + float(score2) + float(score3))/3.0


def main():
    first_name = input('Student\'s first name: ')
    last_name = input('Student\'s last name: ')
    age = input('Student\'s age: ')
    score1 = input('first score: ')
    score2 = input('second score: ')
    score3 = input('third score: ')
    average_scores = average(score1, score2, score3)
    print(last_name + ', ' + first_name + ': age ' + age, end=',')
    print(' average grade: {0:.2f}'.format(average_scores))


if __name__ == '__main__':
    main()