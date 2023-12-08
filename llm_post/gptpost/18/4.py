```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    
    # Postcondition: The return value is equal to the count of non-overlapping occurrences of the substring in the string, plus one if the last occurrence is overlapping.
    assert return_val == string.count(substring) + (1 if string.endswith(substring) else 0)
```