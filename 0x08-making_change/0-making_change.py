#!/usr/bin/python3
"""
Make change depending on the given value
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total.

    Args:
      - coins (list): A list of integers representing the values of
        available coins.
      - total (int): The target total amount to be achieved using the
        available coins.

    Return:
      - int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met by any combination of
             the given coins.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of
    # coins for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, the total cannot be
    # obtained using the given coins
    return dp[total] if dp[total] != float('inf') else -1
