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
    assert all(n % f == 0 for f in return_val), "The factors are not divisors of the input number"
    assert n == return_val[0] * return_val[1] * ... * return_val[-1], "The input number is not equal to the product of its factors"
    return return_val
```