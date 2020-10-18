"""
Program: file_io_assignment.py
Author: Rachael Wolf
Last date modified: 10/12/2020

The purpose of this program is to accept input from the user and write output to a file
"""


def write_to_file(entry, file):
    """Accepts a tuple to append to a file"""
    with open(file, "a") as f:
        f.write(entry)


def get_student_info(file, **kwargs):
    """Accepts a keyword argument for a student name
    Prompts the user to input as many test scores as they wish
    Stores the information (name and scores) in a tuple
    Calls the function write_to_file() sending the tuple to be written to the end of the file"""
    go = True
    storage = []
    for key, value in kwargs.items():
        storage.append("%s = %s" % (key, value))
    score = '0'
    while go:
        score = input('Enter test score, or -1 to finish')
        if score.isdigit() and 0 <= int(score) <= 100:
            storage.append(score)
        elif score == '-1':
            go = False
        else:
            print('invalid input')
    write_to_file(str(storage) + '\n', file)


def read_from_file(filename):
    """Reads a file line by line, and prints each line to the console"""
    with open(filename, "r") as f:
        f.readlines()


def main():
    get_student_info('Student_info.txt', name='Jay Luck')
    get_student_info('Student_info.txt', name='Ashley Graham')
    get_student_info('Student_info.txt', name='Paul Morre')
    get_student_info('Student_info.txt', name='Lisa Hart')
    read_from_file('Student_info.txt')


if __name__ == '__main__':
    main()
