```python
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return_val = []  # Hypothetical return value

    # Postcondition
    assert all(isinstance(num, int) for num in return_val), "The returned list should only contain integers"

    return return_val
```