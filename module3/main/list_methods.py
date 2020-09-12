"""
Program: list_methods.py
Author: Rachael Wolf
Last date modified: 09/12/2020

The purpose of this program is to explore
the methods in python associated with lists.
"""

listOne = ['Rose', 'Zorro', 'Gift']
print(listOne)

# part 1
print(listOne.append('Ralph'))
print(listOne.clear())

# part 2
print(listOne.copy())
print(listOne.count('Gift'))

# part 3
listTwo = ['Ralph', 'Lizzy']
print(listOne.extend(listTwo))
print(listOne.index('Zorro'))
print(listOne.index('Percy'))

# part 4
print(listOne.insert(3, 'Tinker'))
print(listOne.remove('Tinker'))

# part 5
print(listOne.reverse())
print(listOne.sort())
