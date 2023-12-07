#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(limit):
        primes = []
        for i in range(2, limit + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def count_prime_moves(n):
        primes = get_primes(n)
        count = 0

        for prime in primes:
            if n % prime == 0:
                count += 1
        return count

    def play_round(n):
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

    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    else:
        return None
