#!/usr/bin/python3
"""
a module to solve the island  perimeter
"""


def island_perimeter(grid):
    """
    a function to get the island perimerter
    """
    n = len(grid)
    s = 0
    for i in range(1, n - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1 and grid[i - 1][j] == 0:
                s += 1
            if grid[i][j] == 1 and grid[i][j - 1] == 0:
                s += 1
            if grid[i][j] == 1 and grid[i + 1][j] == 0:
                s += 1
            if grid[i][j] == 1 and grid[i][j + 1] == 0:
                s += 1
    return s
