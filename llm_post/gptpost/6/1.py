```python
def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE
    assert isinstance(return_val, list)
    assert all(isinstance(val, int) for val in return_val)
    assert len(return_val) == paren_string.count('()')

    return return_val
```