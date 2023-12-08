```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    assert isinstance(return_val, bool), "Return value must be a boolean"
    assert return_val == (n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))), "Incorrect prime determination"
```
The postcondition asserts that the return value of the function `is_prime` should be a boolean and it accurately determines whether the given number `n` is prime or not.