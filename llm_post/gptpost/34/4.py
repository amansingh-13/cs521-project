```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    assert isinstance(return_val, list)  # The return value is a list
    assert sorted(return_val) == return_val  # The return list is sorted in ascending order
    assert all(x in l for x in return_val)  # All elements in the return list are present in the input list
    assert all(l.count(x) == 1 for x in return_val)  # All elements in the return list are unique
    assert len(return_val) <= len(l)  # The length of the return list is less than or equal to the input list
```