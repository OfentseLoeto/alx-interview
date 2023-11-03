#!/usr/bin/python3
"""
This function aims to solve the N queens problem.
"""
import sys


def is_safe(board, row, col, N):
    """
    Checking if it is safe to place a queen at a given position
    """
    # Checking column on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Checking the upper_left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checking the lower-left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and print all solutions.
    """
    if N < 4:
        print("N must be at least 4\n")
        return 1

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(row):
        if row == N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

    if not solutions:
        print("No solutions found.")
        return 1

    for solution in solutions:
        print(solution)
        print()

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)

    exit_code = solve_nqueens(N)
    sys.exit(exit_code)
