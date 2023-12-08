def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Parameters:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    Examples:
    >>> largest_divisor(15)
    5
    """

    # initialize the largest divisor to 1
    largest_divisor = 1

    # iterate from 2 to n-1
    for i in range(2, n):
        # if i divides n evenly, update the largest divisor
        if n % i == 0:
            largest_divisor = i

    return largest_divisor