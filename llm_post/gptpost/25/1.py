```python
assert isinstance(return_val, list)
assert all(isinstance(factor, int) for factor in return_val)
assert all(n % factor == 0 for factor in return_val)
assert all(factors.count(factor) == return_val.count(factor) for factor in return_val)
assert n == return_val[0] * return_val[1] * ... * return_val[-1]
```