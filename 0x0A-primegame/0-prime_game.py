#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Return a list of primes up to n using the Sieve of Eratosthenes """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """ Determine the winner after x rounds """
    if not nums or x <= 0:
        return None

    # Find the maximum n in nums to optimize the sieve process
    max_n = max(nums)

    # Generate primes up to max_n
    primes = sieve_of_eratosthenes(max_n)

    # Precompute number of prime moves up to each n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Count the wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # For each round
    for n in nums:
        # If the number of prime numbers is odd
        # Maria wins (since she starts first)
        # If it's even, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
