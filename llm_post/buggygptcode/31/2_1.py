def is_prime(n):
    # Check if n is less than 2, in which case it is not prime
    if n < 2:
        return False
    
    # Check if n is divisible by any number from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True