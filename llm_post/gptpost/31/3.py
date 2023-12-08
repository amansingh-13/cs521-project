```python
assert (n == 1 and not return_val) or (n != 1 and all(n % i != 0 for i in range(2, n)) == return_val)
```