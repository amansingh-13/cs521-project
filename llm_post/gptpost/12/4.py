```python
assert (
    (strings == [] and return_val is None) or
    (strings != [] and return_val == max(strings, key=len))
)
```