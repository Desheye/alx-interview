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
    last_prime = primes[-1]
    if limit > last_prime:
        for i in range(last_prime + 1, limit + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def get_winner(num_rounds, rounds_list):
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
    prime_nums = [0, 0, 2]

    compute_primes(max(rounds_list), prime_nums)

    for rnd in range(num_rounds):
        prime_count = sum((i != 0 and i <= rounds_list[rnd])
                          for i in prime_nums[:rounds_list[rnd] + 1])

        if prime_count % 2:
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"

    return None
