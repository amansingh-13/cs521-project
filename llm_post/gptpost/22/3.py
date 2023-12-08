```python
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Hypothetical return value
    return_val = []
    
    # Symbolic postcondition
    assert all(isinstance(val, int) for val in return_val)
    
    return return_val
```