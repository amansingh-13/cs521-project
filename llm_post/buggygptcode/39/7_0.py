# To find the n-th number that is a Fibonacci number and prime, we can generate Fibonacci numbers until we find one that is prime.
# We can use a helper function to check if a number is prime.

def is_prime(n: int) -> bool:
    """
    is_prime returns True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    fib_seq = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    count = 2  # Start counting from the third number
    while count < n:
        next_number = fib_seq[-1] + fib_seq[-2]  # Calculate the next Fibonacci number
        if is_prime(next_number):  # Check if the next number is prime
            count += 1
        fib_seq.append(next_number)  # Append the next number to the Fibonacci sequence
    return fib_seq[-1]  # Return the last number in the Fibonacci sequence