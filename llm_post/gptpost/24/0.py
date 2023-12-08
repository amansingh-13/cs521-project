```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert isinstance(n, int), "Input parameter n must be an integer"
    assert n > 0, "Input parameter n must be a positive integer"
    assert return_val > 0, "The largest divisor must be a positive integer"
    assert n % return_val == 0, "The largest divisor must evenly divide the input number"
    assert return_val < n, "The largest divisor must be smaller than the input number"
    # Your implementation here
```