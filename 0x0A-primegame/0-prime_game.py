#!/usr/bin/python3
"""
Prime game
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

    def get_primes(limit):
        """
        Generates a list of prime numbers up to a given limit.

        Args:
        - limit (int): The upper limit for generating prime numbers.

        Returns:
        - list: List of prime numbers.
        """
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False
        return [num for num in range(limit + 1) if primes[num]]

    def count_prime_moves(n):
        """
        Counts the number of prime moves for a given number n.

        Args:
        - n (int): The number for which prime moves are counted.

        Returns:
        - int: The count of prime moves.
        """
        primes = get_primes(n)
        count = 0

        for prime in primes:
            if n % prime == 0:
                count += 1
        return count

    def play_round(n):
        """
        Simulates a round of the prime game for a given number n.

        Args:
        - n (int): The starting number for the round.

        Returns:
        - str: The name of the player who won the round ("Ben" or "Maria").
        """
        while n > 1:
            count = count_prime_moves(n)
            if count % 2 == 0:
                count -= 1
            else:
                n //= 2

        return "Ben" if n == 1 else "Maria"

    ben_wins = 0
    maria_wins = 0

    for i in range(x):
        winner = play_round(nums[i])
        if winner == "Ben":
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner or return None in case of a tie
    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    else:
        return None
