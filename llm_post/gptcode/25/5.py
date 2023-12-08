def factorize(n: int) -> List[int]:
    # Initialize an empty list to store the factors
    factors = []

    # Check if 2 is a factor of n
    while n % 2 == 0:
        factors.append(2)
        n /= 2

    # Check for all odd factors starting from 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n /= i

    # If n is still greater than 2, it means n itself is a prime factor
    if n > 2:
        factors.append(n)

    return factors