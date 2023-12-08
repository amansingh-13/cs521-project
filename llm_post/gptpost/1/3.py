```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # POSTCONDITION
    assert isinstance(return_val, list)  # The return value is a list
    assert all(isinstance(x, str) for x in return_val)  # Each element in the list is a string
    assert all(x.count("(") == x.count(")") for x in return_val)  # Each string has balanced parentheses
    assert all("(" not in x and ")" not in x for x in return_val)  # No string contains any parentheses
    assert ''.join(return_val) == paren_string.replace(" ", "")  # The concatenation of the strings is equal to the input string without spaces
```