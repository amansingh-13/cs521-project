```python
assert isinstance(return_val, int)  # The return value should be an integer
assert return_val >= 0  # The return value should be greater than or equal to zero
assert string.count(substring) >= return_val  # The count of substring in the string should be greater than or equal to the return value
assert string.count(substring) <= return_val + string.count(substring[len(substring) - 1:])  # The count of substring in the string should be less than or equal to the return value plus the count of the last character of substring in the string
```