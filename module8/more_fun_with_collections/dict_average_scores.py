"""
Program: dict_average_scores.py
Author: Rachael Wolf
Last date modified: 10/19/2020

The purpose of this program is to get a student's first and
last names, their age, and three scores as input, then output
the mame, age, and average score. This is an updated version
of average_scores.py
"""


def get_test_scores():
    """Creates an empty dictionary
    Prompts the user to input the number of test scores
    Prompts the user to input the scores, one by one
    from these inputs, creates a dictionary of scores
    :returns a dictionary of scores"""
    scores_dict = dict()
    num_scores = input("How many scores? ")
    while not num_scores.isdigit() or int(num_scores) < 1:
        print("There must be at least one score")
        num_scores = input("How many scores? ")
    for n in range(1, int(num_scores) + 1):
        score = input("Enter score #" + str(n) + ": ")
        if not score.isdigit() or int(score) < 0:
            raise ValueError
        else:
            scores_dict.update({str(n): int(score)})
    return scores_dict


def average_scores(score_dict):
    """accepts a dictionary of scores and prints the average score report as
     a formatted string"""
    score_sum = 0.0
    print('Result:', end=' ')
    for n in range(1, len(score_dict) + 1):
        score_sum += score_dict[str(n)]
    print('current average {0:.2f}'.format(score_sum/len(score_dict)))
    # return


def get_average_scores(score_dict):
    """accepts a dictionary of scores and returns the average score as
     a float"""
    score_sum = 0.0
    for n in range(1, len(score_dict) + 1):
        score_sum += score_dict[str(n)]
    # print('current average {0:.2f}'.format(score_sum/len(score_dict)))
    return score_sum/len(score_dict)


def main():
    average_scores(get_test_scores())
    # 4 scores: 78, 56, 89, 72 -----------> output: Result: current average 73.75


if __name__ == '__main__':
    main()
