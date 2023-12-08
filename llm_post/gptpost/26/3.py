```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Postcondition: The returned list should not contain any elements that occur more than once
    assert all(numbers.count(num) == 1 for num in numbers)
```

The postcondition asserts that the count of each element in the returned list should be equal to 1, indicating that there are no elements that occur more than once.