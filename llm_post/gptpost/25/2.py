```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    return_val = []  # hypothetical return value
    
    # Postcondition
    assert n == 1 or (all(n % factor == 0 for factor in return_val) and n == return_val.prod())
    
    return return_val
```