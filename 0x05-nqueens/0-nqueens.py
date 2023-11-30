#!/usr/bin/python3
"""
This module provides a program to solve the N-Queens problem,
which is the challenge of placing N non-attacking queens on
an N×N chessboard. The program takes an integer N as a
command-line argument and prints every possible solution to
the problem.
"""
import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    if row == n:
        print([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve_nqueens(board, row + 1, n)


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
