```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Symbolic postcondition
    assert int(return_val, 2) == (int(a, 2) ^ int(b, 2)).bit_length() - 1
```