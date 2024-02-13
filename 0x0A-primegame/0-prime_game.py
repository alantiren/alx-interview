#!/usr/bin/python3
"""Prime game module.
"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of the prime game.
    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper limits for each round.
    Returns:
        str or None: Name of the player who won the most rounds,
        or None if it's a tie.
    """
    def count_primes(num):
        return sum(1 for i in range(2, num + 1) if is_prime(i))

    maria_wins = 0
    ben_wins = 0


    for n in nums:
        num_primes = count_primes(n)

        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1


    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"

if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
