```python
assert isinstance(return_val, float), "Return value must be a float"
assert abs(poly(xs, return_val)) < 0.0001, "The returned zero point does not satisfy the polynomial equation"
assert len(xs) % 2 == 0, "The input list must have an even number of coefficients"
assert max(xs) != 0, "The largest non-zero coefficient must be nonzero"
```