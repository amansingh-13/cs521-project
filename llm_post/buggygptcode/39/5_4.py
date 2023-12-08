def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int) -> bool:
        """
        is_prime checks if a given number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n: int) -> int:
        """
        fibonacci returns the n-th number in the Fibonacci sequence.
        """
        if n < 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    count = 0
    i = 0
    while count < n:
        i += 1
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
    return fib_num