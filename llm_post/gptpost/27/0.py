```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return_val = ...
    
    assert # Postcondition goes here
    
    return return_val
```

```python
# Postcondition:

assert return_val == ''.join([c.lower() if c.isupper() else c.upper() for c in string])
```

The postcondition asserts that the return value is equal to a new string where each lowercase character in the original string is flipped to uppercase and each uppercase character in the original string is flipped to lowercase.