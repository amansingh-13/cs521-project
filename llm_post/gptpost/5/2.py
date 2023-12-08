```python
assert (
    all(
        return_val[i] == numbers[i // 2] if i % 2 == 0 else return_val[i] == delimeter
        for i in range(len(return_val))
    )
)
```