"""
Program: better_average_scores.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to get a student's first and
last names, their age, and three scores as input, then output
the mame, age, and average score. This is an updated version
of average_scores.py
"""


def average_scores(*args, **kwargs):
    print('Result:', end=' ')
    for key, value in kwargs.items():
        print("%s = %s" % (key, value), end=' ')
        # Use *args for average calculation
    score_sum = 0.0
    for n in args:
        if n < 0:
            raise ValueError
        else:
            score_sum += n
    print('with current average {0:.2f}'.format(score_sum/len(args)))
    # return


def main():
    average_scores(84, 72, 65, 92, name='Jay Luck', gpa=3.4, course='German')
    average_scores(72, 85, 83, 67, 78, name='Ashley Graham', gpa=3.2, course='Psychology of Horror Literature')
    average_scores(53, 81, 75, 92, 89, 74, name='Paul Morre', gpa=2.7, course='Statistics')


if __name__ == '__main__':
    main()
