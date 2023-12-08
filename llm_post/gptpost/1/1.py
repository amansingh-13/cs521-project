```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

# Postcondition: The return value is a list of strings where each string represents a separate group of balanced parentheses from the input paren_string. There are no nested groups within each string and any spaces in the input string are ignored.
return_val == ['()', '(())', '(()())']
assert all(isinstance(s, str) for s in return_val)
assert all(s.count('(') == s.count(')') for s in return_val)
assert all('(' not in s and ')' not in s for s in return_val)
```