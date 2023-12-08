```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    assert isinstance(return_val, str)
    assert len(return_val) == len(string)
    assert all((c.islower() and return_val[i].isupper()) or (c.isupper() and return_val[i].islower()) or c == return_val[i] for i, c in enumerate(string))
```