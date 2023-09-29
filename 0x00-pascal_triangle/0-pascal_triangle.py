#!/usr/bin/python3
"""
Function that returns a list of lists of
integers representing the Pascal’s triangle
"""

def pascal_triangle(n):

    if n <= 0:
        return []

    # Initialize an empty list to store the triangle
    triangle = []

    for i in range(n):
        # Initialize an empty list for each row
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:

                # The first and last elements in each row are always 1
                row.append(1)

            else:
                 # Other elements are the sum of the two elements above
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Add the row to the triangle
        triangle.append(row)

    return triangle
