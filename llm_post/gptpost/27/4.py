```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return_val = ""

    for char in string:
        if char.islower():
            return_val += char.upper()
        else:
            return_val += char.lower()

    assert all((c.islower() and return_val[i].isupper()) or (c.isupper() and return_val[i].islower()) or c == return_val[i] for i, c in enumerate(string))
```