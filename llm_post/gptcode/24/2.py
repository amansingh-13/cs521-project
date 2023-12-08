def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start with the largest divisor being n-1
    divisor = n - 1

    # Keep checking if the divisor divides n evenly
    while divisor > 0:
        if n % divisor == 0:
            return divisor
        divisor -= 1

    # If no divisor is found, return None
    return None