```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    return_val = []
    min_val = min(numbers)
    max_val = max(numbers)
    for num in numbers:
        new_val = (num - min_val) / (max_val - min_val)
        return_val.append(new_val)
    return return_val

# Postcondition
assert all(0 <= val <= 1 for val in return_val)
```