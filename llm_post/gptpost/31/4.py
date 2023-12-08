```
assert isinstance(return_val, bool)  # The return value should be a boolean
assert return_val == (n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)))  # The return value should be True if and only if the number is prime
```