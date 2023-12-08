```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    
    # Postcondition: The length of the concatenated string is equal to the sum of the lengths of all input strings
    assert len(return_val) == sum(len(s) for s in strings)
```