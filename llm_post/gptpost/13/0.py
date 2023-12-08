```python
assert isinstance(return_val, int), "Return value should be an integer"
assert a % return_val == 0 and b % return_val == 0, "Return value should be a common divisor of a and b"
assert all(a % i != 0 or b % i != 0 for i in range(2, return_val)), "Return value should be the greatest common divisor of a and b"
```