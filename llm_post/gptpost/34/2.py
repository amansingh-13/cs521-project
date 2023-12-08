```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    assert isinstance(return_val, list), "Return value must be a list"
    assert all(x in l for x in return_val), "All elements in return value must be present in original list"
    assert all(x in return_val for x in l), "All elements in original list must be present in return value"
    assert sorted(return_val) == return_val, "Return value must be sorted in ascending order"
    assert len(return_val) == len(set(return_val)), "Return value must contain unique elements only"
```