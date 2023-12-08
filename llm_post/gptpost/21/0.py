```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert isinstance(numbers, list), "Input must be a list"
    assert len(numbers) >= 2, "Input list must have at least two elements"
    assert isinstance(numbers[0], float), "Elements of the list must be floats"
    assert all(isinstance(num, float) for num in numbers), "Elements of the list must be floats"
    assert return_val[0] == 0, "The smallest number should be transformed to 0"
    assert return_val[-1] == 1, "The largest number should be transformed to 1"
    assert return_val[i] > return_val[j] for i in range(len(return_val)) for j in range(i+1, len(return_val)), "The transformed list should be sorted in ascending order"
```