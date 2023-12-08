```python
assert (
    (len(strings) == 0 and return_val is None) or
    (len(strings) > 0 and return_val in strings and all(len(s) <= len(return_val) for s in strings))
)
```