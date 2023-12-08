def factorize(n: int) -> List[int]:
    factors = []
    # iterate from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # check if i is a factor of n
        while n % i != 0:
            factors.append(i)
            # divide n by i until it is no longer divisible
            n //= i
    
    # if n is still greater than 1, it is a prime number
    if n > 1:
        factors.append(n)
    
    return factors