```python
assert isinstance(return_val, tuple)
assert len(return_val) == 2
assert isinstance(return_val[0], float)
assert isinstance(return_val[1], float)
assert return_val[0] <= return_val[1]
assert abs(return_val[0] - return_val[1]) == min(abs(numbers[i] - numbers[j]) for i in range(len(numbers)) for j in range(len(numbers)) if i != j)
```