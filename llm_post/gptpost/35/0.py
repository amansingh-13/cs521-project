```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    assert isinstance(return_val, int), "return_val should be an integer"
    assert return_val in l, "return_val should be an element in the list"
    assert all(x <= return_val for x in l), "return_val should be the maximum element in the list"
```