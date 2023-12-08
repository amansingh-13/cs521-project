```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Symbolic Postcondition
    assert isinstance(return_val, int) 
    assert (string.lower() != "") == (return_val > 0) 
    assert (string.lower() == "") == (return_val == 0) 
    assert return_val >= 0
    assert return_val <= len(string)
    assert return_val <= 26
    assert return_val == len(set(string.lower()))
```