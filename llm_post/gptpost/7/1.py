```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    assert isinstance(return_val, list)
    assert all(isinstance(s, str) for s in return_val)
    assert all(substring in s for s in return_val)
    assert all(s in strings for s in return_val)
    assert all(s in return_val for s in strings if substring in s)
    assert len(return_val) <= len(strings)
    assert all(s in strings for s in return_val) or len(return_val) == 0
    assert all(substring in s for s in return_val) or len(return_val) == 0
    assert set(return_val) <= set(strings)
```