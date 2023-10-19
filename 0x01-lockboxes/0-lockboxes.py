#!/usr/bin/python3
"""
Writing a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    n = len(boxes)
    # Keeping track of the visited boxes
    visited = [False] * n
    # The first boxe is already opened
    visited[0] = True

    # Using stack to perform depth-first search
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
