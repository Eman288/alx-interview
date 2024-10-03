#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    mylist = []
    mylist.insert(0, [1])
    for i in range(1, 5):
        oldlist = mylist[i - 1]
        newlist = []
        for j in range(i + 1):
            if j == 0 or j == i:
                newlist.insert(j, 1)
            else:
                newlist.insert(j, oldlist[j] + oldlist[j - 1])
        mylist.insert(i, newlist)
    return mylist
