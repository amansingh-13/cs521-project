```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return_val = ""
    
    # POSTCONDITION
    assert len(return_val) == len(a) == len(b), "The length of the return value should be equal to the lengths of both input strings"
    assert all((return_val[i] == '1' and a[i] != b[i]) or (return_val[i] == '0' and a[i] == b[i]) for i in range(len(return_val))), "The return value should be the result of binary XOR operation on the input strings" 
    
    return return_val
```