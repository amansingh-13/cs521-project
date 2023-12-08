```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    
    # Symbolic postcondition
    assert all(string in return_val for string in strings if substring in string) == (return_val == [string for string in strings if substring in string])
```