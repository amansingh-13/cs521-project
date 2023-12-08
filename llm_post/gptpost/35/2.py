```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    
    assert (all(return_val >= x for x in l) and return_val in l) or (all(return_val < x for x in l) and return_val not in l)
```