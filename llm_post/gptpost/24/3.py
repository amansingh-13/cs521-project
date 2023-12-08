```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    assert isinstance(n, int), "Input should be an integer"
    assert n > 0, "Input should be a positive number"

    # Hypothetical return value
    return_val = 0

    # Postcondition
    assert return_val < n, "The largest divisor should be smaller than n"
    assert n % return_val == 0, "The largest divisor should evenly divide n"

    return return_val
```
The postcondition checks that the hypothetical return value is smaller than the input number `n`, and that `n` is evenly divisible by the return value.