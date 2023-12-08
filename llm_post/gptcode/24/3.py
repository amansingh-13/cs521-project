def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly and is smaller than n.
    """
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            largest = i
    return largest