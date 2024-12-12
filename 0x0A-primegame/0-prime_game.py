#!/usr/bin/python3
"""
a module to solve the prime game
"""


def GetPrimes(num):
    """
    a function to get all the prime numbers from 2 to num
    """
    numbersRange = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (numbersRange[p]):
            for i in range(p * p, num + 1, p):
                numbersRange[i] = False
        p += 1
    primes = []
    for p in range(2, num + 1):
        if (numbersRange[p]):
            primes.append(p)
    return primes


def isWinner(x, nums):
    """
    a function to solve the prime game
    """
    n = len(nums)
    b = 0
    m = 0
    i = 0
    while (i < x):
        if (len(GetPrimes(nums[i])) % 2 == 0):
            b += 1
        else:
            m += 1
        i += 1
    if (b > m):
        return "Ben"
    elif (m > b):
        return "Maria"
    else:
        return None
