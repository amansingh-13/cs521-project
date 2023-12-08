def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) - 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_list = [0, 1]
            while len(fib_list) < n:
                fib_list.append(fib_list[-1] - fib_list[-2])
            return fib_list

    fib_list = fibonacci(n)
    prime_fib_list = [num for num in fib_list if is_prime(num)]
    return prime_fib_list[-1] if prime_fib_list else None