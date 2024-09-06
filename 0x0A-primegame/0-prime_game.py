#!/usr/bin/python3

"""
Prime Game Algorithm (Python)
"""


def is_prime(n):
    """
    Checks if a number is prime.
    Args:
        n (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def compute_primes(limit, primes):
    """
    Generates all prime numbers up to a specified limit.
    Args:
        limit (int): Maximum number to check for primes.
        primes (list): List to store the primes.
    """
    last_prime = primes[-1] if primes else 1
    for i in range(last_prime + 1, limit + 1):
        if is_prime(i):
            primes.append(i)


def isWinner(num_rounds, rounds_list):
    """
    Determines the player who won the most rounds.
    Args:
        num_rounds (int): The total number of rounds.
        rounds_list (list): List of numbers for each round.
    Returns:
        str or None: 'Maria' or 'Ben' as the winner,
                     or None if no winner.
    """
    wins = {"Maria": 0, "Ben": 0}
    primes = []

    compute_primes(max(rounds_list), primes)

    for rnd in range(num_rounds):
        prime_count = sum(1 for p in primes if p <= rounds_list[rnd])

        if prime_count % 2 == 1:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"

    return None
