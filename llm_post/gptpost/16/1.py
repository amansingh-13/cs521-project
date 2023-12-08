```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Postcondition: The number of distinct characters in the string is equal to the length of a set created from the string with all characters converted to lowercase.
    assert isinstance(return_val, int)
    assert return_val == len(set(string.lower()))
```