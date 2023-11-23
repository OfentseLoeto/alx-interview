#!/usr/bin/python3
"""
Make change depending on the given value
"""


def makeChange(coins, total):
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
