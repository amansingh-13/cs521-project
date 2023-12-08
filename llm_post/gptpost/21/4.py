```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    n = len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    
    return_val = []
    for num in numbers:
        transformed_num = (num - min_val) / (max_val - min_val)
        return_val.append(transformed_num)
    
    return return_val

# Postcondition
assert all(0 <= num <= 1 for num in return_val)
```