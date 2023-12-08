```python
assert isinstance(return_val, float)  # The return value should be a float
assert abs(poly(xs, return_val)) < 1e-6  # The polynomial evaluated at the return value should be close to zero
assert all(abs(poly(xs, x)) > 1e-6 for x in [-1, return_val, 1])  # The polynomial evaluated at -1, 1, and the return value should not be close to zero
```