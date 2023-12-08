def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    """

    # Start with the largest possible divisor, which is n - 1
    divisor = n - 1

    # Loop until a divisor is found or divisor becomes 1
    while divisor > 1:
        # Check if n is evenly divisible by divisor
        if n % divisor != 0:
            # Return the divisor
            return divisor
        # Decrement the divisor by 1
        divisor -= 1

    # If no divisor is found, return None
    return None