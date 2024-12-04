#!/usr/bin/python3
"""
a module to solve the island  perimeter
"""


def island_perimeter(grid):
    """
    a function to get the island perimerter
    """
    n = len(grid)
    m = len(grid[0])
    s = 0
    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == 1:
                if i != 0 and grid[i - 1][j] == 0:
                    s += 1
                if j != 0 and grid[i][j - 1] == 0:
                    s += 1
                if i != n - 1 and grid[i + 1][j] == 0:
                    s += 1
                if j != m - 1 and grid[i][j + 1] == 0:
                    s += 1
    return s
