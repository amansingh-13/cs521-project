```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    assert isinstance(return_val, str), "The return value should be a string"
    assert len(return_val) == sum(len(s) for s in strings), "The length of the return value should be equal to the sum of lengths of all strings"
    for s in strings:
        assert s in return_val, "All strings in the input list should be present in the return value (order may vary)"
```