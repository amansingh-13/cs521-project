```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    assert isinstance(return_val, str) or return_val is None, "Return value should be a string or None"
    assert return_val in strings or return_val is None, "Return value should be present in the input list or None if the input list is empty"
    assert all(len(s) <= len(return_val) for s in strings), "The length of return value should be greater than or equal to the length of all strings in the input list"
    assert all(len(s) < len(return_val) or s == return_val for s in strings), "There should not be any string in the input list with greater length than the return value, except if they are equal to the return value"
    return return_val
```