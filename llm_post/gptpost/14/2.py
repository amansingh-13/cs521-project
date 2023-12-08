```python
assert isinstance(return_val, list)
assert all(isinstance(prefix, str) for prefix in return_val)
assert all(return_val[i] == string[:i+1] for i in range(len(return_val)))
```