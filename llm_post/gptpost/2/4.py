```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    assert isinstance(return_val, float), "The return value should be a float."
    assert return_val >= 0 and return_val < 1, "The return value should be in the range [0, 1)."
    assert return_val == number - int(number), "The return value should be equal to the difference between the number and its integer part."
    return return_val
```