```python
assert isinstance(return_val, bool)
assert return_val == True if any(sum(operations[:i+1]) < 0 for i in range(len(operations))) else False
```