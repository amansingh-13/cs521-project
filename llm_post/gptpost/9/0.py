```python
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    
    # Postcondition:
    assert all(return_val[i] >= max(numbers[:i+1]) for i in range(len(numbers)))
    
    return return_val
```