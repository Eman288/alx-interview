#!/usr/bin/env python3
"""a module to complete the minimum operations challenge"""


def minOperations(num: int) -> int:
    """
        a function to return the sum of the prime factors for a number
    """
    s = 0
    i = 0
    while num % 2 == 0:
        s += 2
        num //= 2
    for i in range(3, int(num**0.5) + 1):
        if num % i == 0:
            s += i
            num //= i
            i -= 1
        else:
            i += 1
    if num > 2:
        s += num
    return s
