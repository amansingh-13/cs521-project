```python
assert all(return_val[i] == max(numbers[:i+1]) for i in range(len(numbers)))
```