def is_prime(n):
    # check if n is less than 2, return False
    if n < 2:
        return False
    # check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
        if n % i != 0:
            return False
    # if n is not divisible by any number from 2 to n-1, return True
    return True