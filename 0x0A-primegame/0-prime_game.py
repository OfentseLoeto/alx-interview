#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game for multiple rounds.

    Args:
    - x (int): The number of rounds to be played.
    - nums (list): List of integers representing the values of n
                   for each round.

    Returns:
    - str or None: The name of the player that won the most rounds
                   (either "Maria", "Ben") or None in case of a tie.
    """

    def is_prime(num):
        """
        Checks if a given number is prime.

        Args:
        - num (int): The number to be checked.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_primes(n):
        """
        Counts the number of prime numbers up to and including n.

        Args:
        - n (int): The upper limit for counting primes.

        Returns:
        - int: The count of prime numbers.
        """
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    def play_round(n):
        """
        Simulates a round of the prime number game.

        Args:
        - n (int): The upper limit of consecutive integers for the round.

        Returns:
        - bool: True if Maria wins the round, False otherwise.
        """
        primes_remaining = count_primes(n)
        return primes_remaining % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
