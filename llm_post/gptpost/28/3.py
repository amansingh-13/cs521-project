```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return_val = ''  # hypothetical return value
    
    assert return_val == ''.join(strings)  # Postcondition: The return value is equal to the concatenation of all the strings in the input list
```