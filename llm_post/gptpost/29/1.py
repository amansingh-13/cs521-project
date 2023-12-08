```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    
    # Postcondition: All elements in the returned list start with the given prefix
    return_val = []
    assert all([s.startswith(prefix) for s in return_val])
    return return_val
```