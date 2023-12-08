```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return_val = 0 # hypothetical return value
    
    # Postcondition
    assert isinstance(return_val, int), "Return value must be an integer"
    assert return_val >= 0, "Return value must be non-negative"
    assert len(set(string.lower())) == return_val, "Return value must be equal to the number of distinct characters in the string"
```