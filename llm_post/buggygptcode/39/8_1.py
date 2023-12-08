def prime_fib(n: int):
    def is_prime(num):
        """
        is_prime checks if a number is prime or not.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n):
        """
        fib returns the n-th Fibonacci number.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    count = 0
    i = 1
    while count < n:
        num = fib(i)
        if is_prime(num):
            count += 1
        i += 1
    return num