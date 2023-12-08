```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return_val = 0
    # Postcondition: The return value is the actual count of the digit 7 in integers less than n that are divisible by 11 or 13.
    assert return_val == sum(str(i).count('7') for i in range(n) if i % 11 == 0 or i % 13 == 0)
```