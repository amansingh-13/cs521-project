```python
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    assert isinstance(return_val, float), "Return value should be a float"
    assert return_val >= 0, "Return value should be greater than or equal to 0"
    assert abs(return_val - sum(abs(x - return_val) for x in numbers) / len(numbers)) < 1e-9, "Return value should be equal to the mean absolute deviation of numbers"
```