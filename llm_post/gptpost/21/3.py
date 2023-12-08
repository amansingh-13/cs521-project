```python
assert len(return_val) == len(numbers)
assert all(0 <= num <= 1 for num in return_val)
assert all(num == 0 or num == 1 for num in [return_val[0], return_val[-1]])
assert return_val[0] == 0
assert return_val[-1] == 1
```