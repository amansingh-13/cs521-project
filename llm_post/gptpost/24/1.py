```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE
    assert return_val > 1 and return_val < n and n % return_val == 0
```