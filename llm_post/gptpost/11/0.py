```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Symbolic postcondition
    assert all(int(a[i]) + int(b[i]) == 1 for i in range(len(a))) or all(int(a[i]) + int(b[i]) == 2 for i in range(len(a))), "Invalid postcondition"
```