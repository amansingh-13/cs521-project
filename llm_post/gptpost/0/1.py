```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    return_val = False
    # Postcondition: If return_val is True, then there exists i and j such that 
    # i != j and abs(numbers[i] - numbers[j]) < threshold
    assert (return_val == False) or (return_val == True and 
                                     any(abs(numbers[i] - numbers[j]) < threshold 
                                         for i in range(len(numbers)) 
                                         for j in range(len(numbers)) if i != j))
```