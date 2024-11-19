#!/usr/bin/python3
"""
a module to rotate a matric 90deg
"""


def rotate_2d_matrix(matrix):
    """
    a function to rotate a matrics 90deg
    """
    copyMat = []
    n = len(matrix)
    for i in range(n):
        r = []
        for j in range(n):
            r.append(matrix[n - j - 1][i])
        copyMat.append(r)

    for i in range(n):
        for j in range(n):
            matrix[i][j] = copyMat[i][j]
