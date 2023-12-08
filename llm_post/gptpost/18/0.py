```python
assert isinstance(return_val, int) # The return value is an integer
assert return_val >= 0 # The return value is non-negative
assert return_val <= len(string) # The return value is less than or equal to the length of the original string
assert isinstance(string, str) # The input string is a string
assert isinstance(substring, str) # The input substring is a string
assert substring != '' # The input substring is not an empty string
assert return_val == sum([1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]) # The return value is equal to the number of times the substring appears in the original string, including overlapping cases
```