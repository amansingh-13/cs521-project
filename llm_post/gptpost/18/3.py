```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    assert isinstance(return_val, int), "The return value should be an integer."
    assert return_val >= 0, "The return value should be non-negative."
    assert return_val <= len(string), "The return value should not exceed the length of the original string."
    assert return_val <= len(string) - len(substring) + 1, "The return value should not exceed the number of possible overlapping occurrences."
    assert return_val == string.count(substring), "The return value should be equal to the number of occurrences of the substring in the string."
```