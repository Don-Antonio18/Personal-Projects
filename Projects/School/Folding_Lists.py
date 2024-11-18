"""
Write listSum that takes a list as argument, and
returns the sum of the elements in the list
e.g. listSum ([2, 3, 5, 7, 11]) → 28
"""

def listSum(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + listSum(lst[1:])
    
"""Write listProd that takes a list as argument, and
returns the product of the elements in the list
e.g. listProd ([5, 5, 7]) → 175 """

def listProd(lst):
    if lst == []:
        return 1
    else:
        return lst[0] * listProd(lst[1:])
    
"""Write listMax that takes a list of positive numbers, and
returns the largest element in the list. If the list is empty, it
should return 0.
e.g. listMax ([2, 5, 3, 11, 7, 4]) → 11
Hint: use max; e.g. max(5,3) → 5, max(2, 7) → 7 """

def listMax(lst):
    if lst == []:
        return 0
    else:
        return max(lst[0], listMax(lst[1:]))