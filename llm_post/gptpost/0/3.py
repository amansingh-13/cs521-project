```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    assert isinstance(return_val, bool), "The return value should be of type bool"
    assert all(abs(numbers[i] - numbers[j]) > threshold for i in range(len(numbers)) for j in range(i + 1, len(numbers))), "The function should return True if any two numbers are closer to each other than the threshold, otherwise it should return False"
```