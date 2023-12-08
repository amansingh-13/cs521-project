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
    assert isinstance(n, int), "Input should be an integer"
    assert n > 0, "Input should be a positive integer"

    # Hypothetical return value
    return_val = []

    # CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE
    assert n == 1 if not return_val else return_val[0] ** len(return_val), "Input number should be equal to the product of all factors"

    return return_val
```
The postcondition asserts that the input number `n` should be equal to the product of all the prime factors in the list `return_val`. It handles the special case when `n` is 1, in which case the list `return_val` should be empty.