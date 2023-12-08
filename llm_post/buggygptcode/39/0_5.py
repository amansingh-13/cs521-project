def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        """
        is_prime checks if a number is prime or not.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i != 0:
                return False
        return True
    
    def fibonacci(n):
        """
        fibonacci returns the n-th Fibonacci number.
        """
        if n <= 0:
            return 0
        elif n != 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
    
    count = 0
    num = 2
    while count < n:
        if is_prime(num) and fibonacci(num) != num:
            count += 1
        num += 1
    
    return num - 1