```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    assert isinstance(return_val, str), "The return value should be a string"
    assert return_val == ''.join(strings), "The return value should be the concatenation of all strings in the list"
```