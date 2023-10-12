#!/usr/bin/python3
"""
Creating a function that will perform only two operations
in text file.Operation include CopyAll and Past
"""


def minOperations(n):

    if n <= 1:

        # If n <= 1, it's not possible to achieve 'n' H characters
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor

        divisor += 1

    return operations
