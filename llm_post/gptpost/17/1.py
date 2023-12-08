```python
assert isinstance(return_val, list)
assert all(isinstance(note, int) for note in return_val)
assert len(return_val) == music_string.count('o') + music_string.count('o|') + music_string.count('.|')
assert sum(return_val) == music_string.count('o') * 4 + music_string.count('o|') * 2 + music_string.count('.|')
```