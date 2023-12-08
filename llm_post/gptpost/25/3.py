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
    assert isinstance(return_val, list), "The return value should be a list"
    assert all(isinstance(factor, int) for factor in return_val), "All factors should be integers"
    assert len(return_val) > 0, "The return list should not be empty"
    assert n == 1, "The input number should be equal to the product of all factors"
    assert all(n % factor == 0 for factor in return_val), "All factors should divide the input number evenly"
    assert all(factorize_elem(factor) for factor in return_val), "Each factor should be prime and listed the correct number of times"
    return return_val
```

In the postcondition, we assert the following conditions:
1. The return value should be a list.
2. All factors in the return list should be integers.
3. The return list should not be empty.
4. The input number should be equal to the product of all factors.
5. All factors in the return list should divide the input number evenly.
6. Each factor in the return list should be prime and appear the correct number of times, which is handled by the `factorize_elem()` function.