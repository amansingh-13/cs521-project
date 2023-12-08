```python
assert isinstance(return_val, list)
assert all(isinstance(note, int) for note in return_val)
assert all(note in [1, 2, 4] for note in return_val)
assert sum(return_val) == 24
```