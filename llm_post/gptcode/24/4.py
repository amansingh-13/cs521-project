def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    """
    largest = 0
    for i in range(1, n):
        if n % i == 0:
            largest = i
    return largest

print(largest_divisor(15))