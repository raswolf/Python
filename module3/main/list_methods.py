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
        listOne.append('Ralph')
        print('Append "Ralph": ' + str(listOne))
        listOne.clear()
        print('Clear: ' + str(listOne))
    if index == '2':
        print('Copy: ' + str(listOne.copy()))
        print('Count "Gift": ' + str(listOne.count('Gift')))
    if index == '3':
        listOne.extend(listTwo)
        print('Extend with ' + str(listTwo) + ': ' + str(listOne))
        print('Index "Zorro": ' + str(listOne.index('Zorro')))
        print('Index "Percy": ' + str(listOne.index('Percy')))
    if index == '4':
        listOne.insert(3, 'Tinker')
        print('Insert "Tinker" at 3: ' + str(listOne))
        listOne.remove('Tinker')
        print('Remove "Tinker": ' + str(listOne))
    if index == '5':
        listOne.reverse()
        print('Reverse: ' + str(listOne))
        listOne.sort()
        print('Sort: ' + str(listOne))


if __name__ == '__main__':
    main()
