```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    assert isinstance(return_val, list), "Return value should be a list"
    assert len(return_val) == len(set(return_val)), "Return value should only contain unique elements"
    assert sorted(return_val) == return_val, "Return value should be sorted in ascending order"
    # Additional postconditions can be added here if necessary

    return return_val
```
This postcondition consists of three assert statements that check the following aspects of the function:
1. The return value should be a list.
2. The return value should only contain unique elements (no duplicates).
3. The return value should be sorted in ascending order.