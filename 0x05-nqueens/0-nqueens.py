#!/usr/bin/python3
"""
    a module to get all the solutions for the n-queens problem
"""
import sys


def solveNQueens(n):
    """
    Solves the n-queens problem and returns all valid solutions.
    """
    # This will store all the solutions in terms of column positions for each
    # row
    solutions = []

    # Column, Diagonal 1, Diagonal 2 trackers
    attacked_columns = [False] * n
    attacked_diag1 = [False] * (2 * n - 1)
    attacked_diag2 = [False] * (2 * n - 1)

    # This will store the current column of queens for each row
    current_solution = [-1] * n

    def backtrack(row):
        # If we've placed queens in all rows, we found a solution
        if row == n:
            solutions.append(current_solution[:])  # Store the solution
            return

        for col in range(n):
            # Check if the column or diagonals are attacked
            if (
                attacked_columns[col] or
                attacked_diag1[row - col + n - 1] or
                attacked_diag2[row + col]
            ):
                continue

            # Place queen on the current row, column
            current_solution[row] = col
            attacked_columns[col] = attacked_diag1[row - col + n - 1] = True
            attacked_diag2[row + col] = True

            # Move to the next row
            backtrack(row + 1)

            # Backtrack, remove queen and reset attacks
            attacked_columns[col] = attacked_diag1[row - col + n - 1] = False
            attacked_diag2[row + col] = False
            current_solution[row] = -1

    # Start solving from the first row
    backtrack(0)

    return solutions


def printSolution(sol):
    """
        a function to print the solution in a list like
    """
    solList = []
    for i in range(len(sol)):
        solList.append([i, sol[i]])
    print(solList)


def main():
    """
    Main function to take input and solve the n-queens problem.
    """
    num = sys.argv
    if len(num) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num = int(num[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if num < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveNQueens(num)
    for solution in solutions:
        # print each solution
        printSolution(solution)


main()
