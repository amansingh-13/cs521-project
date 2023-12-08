def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return None

print(largest_divisor(15))