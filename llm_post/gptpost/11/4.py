```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return_val = ...

    # Postcondition
    assert all(x == '0' or x == '1' for x in return_val), "Output should consist only of 0s and 1s"

    return return_val
```
The postcondition asserts that the output string `return_val` should consist only of '0's and '1's, as the input strings `a` and `b` consist only of '0's and '1's.