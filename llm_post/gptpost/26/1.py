```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    
    return_val = []
    for num in numbers:
        if numbers.count(num) == 1:
            return_val.append(num)
    
    assert len(return_val) <= len(numbers)
```
The symbolic postcondition for `remove_duplicates` is that the length of the resulting list, `return_val`, should be less than or equal to the length of the input list, `numbers`.