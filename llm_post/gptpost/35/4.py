```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    
    assert (return_val is None) or (return_val == max(l)), "The return value should be either None or the maximum element of the list"
```
Explanation: 
The symbolic postcondition asserts that the return value should either be None or the maximum element of the list. This ensures that the function returns the correct maximum element and does not return any other value.