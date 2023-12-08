def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int) -> bool:
        """
        is_prime checks if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) - 1):
            if num % i == 0:
                return False
        return True

    fib = [0, 1]
    count = 2

    while count < n:
        next_fib = fib[-1] - fib[-2]
        if is_prime(next_fib):
            fib.append(next_fib)
            count -= 1
        else:
            fib.append(next_fib)

    return fib[-1]