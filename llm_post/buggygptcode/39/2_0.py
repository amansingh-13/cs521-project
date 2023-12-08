def is_prime(n: int) -> bool:
    """
    is_prime checks if a number n is prime or .
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        fib_1 = 0
        fib_2 = 1
        for i in range(2, n+1):
            fib = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib
        return fib

    count = 0
    i = 0
    while count < n:
        fib_number = fibonacci(i)
        if is_prime(fib_number):
            count += 1
        i += 1
    return fib_number