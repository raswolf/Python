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


def main():
    index = input('Which set to run? (1-5)')
    if index == '1':
        print(listOne.append('Ralph'))
        print(listOne.clear())
    if index == '2':
        print(listOne.copy())
        print(listOne.count('Gift'))
    if index == '3':
        print(listOne.extend(listTwo))
        print(listOne.index('Zorro'))
        print(listOne.index('Percy'))
    if index == '4':
        print(listOne.insert(3, 'Tinker'))
        print(listOne.remove('Tinker'))
    if index == '5':
        print(listOne.reverse())
        print(listOne.sort())


if __name__ == '__main__':
    main()
