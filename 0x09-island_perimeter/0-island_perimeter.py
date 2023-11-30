#!/usr/bin/python3
"""
Calculate the perimeter of the island described in the grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    - grid (list of list of int): A rectangular grid representing the island.
                                  0 represents water, and 1 represents land.

    Returns:
    - int: The perimeter of the island.

    Rules:
    - Each cell is square with a side length of 1.
    - Cells are connected horizontally/vertically, not diagonally.
    - The grid is rectangular, with its width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn’t connected to
      the water surrounding the island).

    Examples:
    >>> grid = [
    ...     [0, 0, 0, 0, 0, 0],
    ...     [0, 1, 0, 0, 0, 0],
    ...     [0, 1, 0, 0, 0, 0],
    ...     [0, 1, 1, 1, 0, 0],
    ...     [0, 0, 0, 0, 0, 0]
    ... ]
    >>> island_perimeter(grid)
    12
    """
    perimeter = 0
    if not grid:
        return perimeter

    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return max(0, perimeter)
