```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Postcondition: The return value is a string consisting of 1s and 0s,
    # where each character in the string is the result of performing binary XOR
    # on the corresponding characters from strings a and b.
    assert all(isinstance(char, str) and char in ('0', '1') for char in return_val)

```