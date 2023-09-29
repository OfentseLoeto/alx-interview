#!/usr/bin/python3
"""
  Pascal triangle
"""
def pascal_triangle(n):
    '''
    Function  that returns a list of lists of
    integers representing the Pascal’s triangle of n
    '''

    n = 5

    if n <= 0:
        return []
    for i in range(n):
        print(''*(n-i), end='')

        print(''.join(map(str, str(11**i))))
