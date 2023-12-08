```python
assert isinstance(return_val, str)
assert len(return_val.split()) == n + 1
assert all(str(i) in return_val.split() for i in range(n + 1))
```