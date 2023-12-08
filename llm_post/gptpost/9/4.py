```python
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    assert isinstance(return_val, list), "Return value should be a list"
    assert all(isinstance(num, int) for num in return_val), "All elements in the return list should be integers"
    assert len(return_val) == len(numbers), "Length of return list should be equal to length of input list"
    assert all(return_val[i] >= return_val[i-1] for i in range(1, len(return_val))), "Elements in the return list should be non-decreasing"
```