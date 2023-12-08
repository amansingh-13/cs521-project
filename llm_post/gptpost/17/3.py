```python
assert isinstance(return_val, list)
assert all(isinstance(note, int) for note in return_val)
assert sum(return_val) == sum([4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
```