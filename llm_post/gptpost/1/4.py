```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    return_val = []  # hypothetical return value
    
    # Postcondition: The return value contains separate strings for each group of nested parentheses in paren_string,
    # where each group is balanced and not nested within each other
    assert all(paren in return_val for paren in paren_string.split())  # Each group is in the return value
    assert all(paren.count('(') == paren.count(')') for paren in return_val)  # Each group is balanced
    assert all('(' not in outer_paren and ')' not in inner_paren for outer_paren in return_val for inner_paren in return_val)  # Groups are not nested within each other
    
    return return_val