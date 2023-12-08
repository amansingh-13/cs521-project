```python
assert (
    (strings == [] and return_val is None)
    or (strings != [] and return_val in strings and all(len(s) <= len(return_val) for s in strings))
)
```