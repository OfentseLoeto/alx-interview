#!/usr/bin/python3
"""
This function creates a 2D Matrix and rotates
it 90 degree clockwise.
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row.
    for i in range(n):
        matrix[i].reverse()
