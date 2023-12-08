```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return_val = []  # hypothetically, the return value is stored in this variable

    # Postcondition
    assert all(substring in s for s in return_val)  # All strings in return_val should contain the substring

    return return_val
```

The symbolic postcondition for filter_by_substring is `assert all(substring in s for s in return_val)`. This postcondition ensures that all the strings in the hypothetical return value `return_val` contain the given substring.