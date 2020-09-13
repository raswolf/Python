"""
Program: list_methods.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to explore
the methods in python associated with lists.
"""

listOne = ['Rose', 'Zorro', 'Gift']
listTwo = ['Ralph', 'Lizzy']
print(listOne)


def set_1():
    print(listOne.append('Ralph'))
    print(listOne.clear())


def set_2():
    print(listOne.copy())
    print(listOne.count('Gift'))


def set_3():
    print(listOne.extend(listTwo))
    print(listOne.index('Zorro'))
    print(listOne.index('Percy'))


def set_4():
    print(listOne.insert(3, 'Tinker'))
    print(listOne.remove('Tinker'))


def set_5():
    print(listOne.reverse())
    print(listOne.sort())


def main():
    index = input('Which set to run? (1-5)')
    if index == 1:
        set_1()
    if index == 2:
        set_2()
    if index == 3:
        set_3()
    if index == 4:
        set_4()
    if index == 5:
        set_5()


if __name__ == '__main__':
    main()
