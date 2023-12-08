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
    mean = sum(numbers) / len(numbers)
    absolute_diff_sum = sum(abs(num - mean) for num in numbers)
    return_val = absolute_diff_sum / len(numbers)

    assert return_val == 1.0
```

This postcondition asserts that the computed return value of the function should be equal to 1.0, as specified in the example testcase.