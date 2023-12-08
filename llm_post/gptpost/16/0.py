```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return_val = 0
    # CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE
    return return_val
```

```python
# Postcondition: The number of distinct characters in the string is equal to the length of the set of characters in the string.
assert return_val == len(set(string))
```