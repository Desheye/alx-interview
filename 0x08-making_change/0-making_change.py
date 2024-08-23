#!/usr/bin/python3
"""
Change-making module: Determines the fewest number of coins
needed to meet a given
total amount when provided with a pile of coins
of different values.
"""

def makeChange(coins, total):
    """
    Calculates the minimum number of coins required
    to reach the specified total.
    
    Args:
        coins (list[int]): A list of coin denominations
        (e.g., [1, 5, 10]).
        total (int): The target amount to achieve
        using the given coins.
    
    Returns:
        int: The minimum number of coins needed, or -1
        if the total cannot be reached.
    """
    if total <= 0:
        return 0
    remaining_amount = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remaining_amount > 0:
        if coin_idx >= n:
            return -1
        if remaining_amount - sorted_coins[coin_idx] >= 0:
            remaining_amount -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
