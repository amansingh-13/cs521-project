def is_prime(n):
    # check if the number is less than 2
    if n < 2:
        return False

    # check if the number is divisible by any number from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True