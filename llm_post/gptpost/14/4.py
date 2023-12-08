```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    
    return_val = ...

    # Postcondition: The length of the return value should be equal to the length of the input string
    # and each prefix in the return value should be a substring of the input string.
    assert len(return_val) == len(string)
    for prefix in return_val:
        assert prefix in string

    return return_val
```