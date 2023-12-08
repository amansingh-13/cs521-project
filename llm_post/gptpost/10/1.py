```python
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    return_val = ''
    assert len(return_val) <= len(string), "The length of the returned string should not exceed the length of the input string."
    assert is_palindrome(return_val), "The returned string should be a palindrome."
    return return_val
```