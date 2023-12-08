```python
assert isinstance(return_val, list)
assert all(isinstance(prefix, str) for prefix in return_val)
assert all(string.startswith(prefix) for prefix in return_val)
assert len(return_val) == len(string) + 1
```