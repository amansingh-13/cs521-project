```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    
    return_val = ...

    # Postcondition
    assert isinstance(return_val, float)
```

Note: The postcondition is asserting that the hypothetical return value (`return_val`) of the function is an instance of the `float` class.