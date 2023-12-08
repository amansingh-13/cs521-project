```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    assert (a % return_val == 0) and (b % return_val == 0), "The greatest common divisor should be a factor of both a and b"
```
Note: In the postcondition, `return_val` represents the hypothetical return value of the function `greatest_common_divisor()`. This postcondition asserts that the greatest common divisor returned by the function should be a factor of both `a` and `b`.