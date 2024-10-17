#!/usr/bin/python3
"""a module to complete the minimum operations challenge"""


def minOperations(n: int) -> int:
    """
        a function to return the sum of the prime factors for a number
    """
    s = 0
    i = 0
    if n <= 1:
        return 0
    while n % 2 == 0:
        s += 2
        n //= 2
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            n //= i
            i -= 1
        else:
            i += 1
    if n > 2:
        s += n
    return s
