```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    
    # Postcondition: The resulting list should not contain any duplicate elements.
    assert all(numbers.count(num) == 1 for num in numbers), "The resulting list should not contain any duplicate elements."
    
    # Implementation of the function continues here...
