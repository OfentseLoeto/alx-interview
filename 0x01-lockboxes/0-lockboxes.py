#!/usr/bin/python3
"""
  Determines if all the boxes can be opened.
  This function checks if all boxes can be opened
  by starting from the first box using (DFS) to
  explore and unlock other boxes

  Args:
      Boxes (list of lists): Each element if a list of key to othe boxes.

  Returns:
      bool: True if all boxes can be opened else False
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
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
