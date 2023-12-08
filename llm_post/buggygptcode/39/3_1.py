def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime or not.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None

    fib_numbers = [0, 1]
    count = 2
    while count < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        if is_prime(fib_numbers[-1]):
            count += 1
    
    return fib_numbers[n]