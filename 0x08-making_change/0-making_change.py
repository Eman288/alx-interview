#!/usr/bin/python3
"""
    a module for makeChane function
"""


def makeChange(coins, total):
    """
        a function to return the least number of coins needed to get the total
    """
    coins.sort()
    coins.reverse()
    n = len(coins)
    s = 0
    for i in range(n):
        if total >= coins[i]:
            s += int(total / coins[i])
            total -= int(total / coins[i]) * coins[i]
    if total != 0:
        return -1
    return s
