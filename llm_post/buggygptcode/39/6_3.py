def is_prime(n: int) -> bool:
    """
    is_prime checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3

    count = 2
    fib1 = 2
    fib2 = 3
    while count < n:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        if is_prime(fib):
            count += 1
    return fib