```python
assert isinstance(return_val, int), "Return value must be an integer"
assert return_val >= 0, "Return value must be non-negative"
assert all(str(i).count('7') > 0 for i in range(n) if i % 11 == 0 or i % 13 == 0) == (return_val == len([i for i in range(n) if i % 11 == 0 or i % 13 == 0 and str(i).count('7') > 0]))
```