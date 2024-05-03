#!/usr/bin/python3
"""
Determining the fewest number of coins needed to meet a given amount
total
"""


def makeChange(coins, total):
    # Initialise a list to store a minimum number of coins neededfor
    # each total to the given total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make a total of 0
    dp[0] = 0

    # Iterate  through all total from 1 to a given total
    for i in range(1, total + 1):
        # For each total, iterate through all coins values
        for coin in coins:
            # If coin is less than or equal to the current total
            # uptate dp[i] with the minimum of thecurrent value of dp[i] and
            # dp[i - coin] + 1
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    # If dp[total] is still float('inf') , it means the total cannot be met
    # by any number of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
