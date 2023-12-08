```
assert isinstance(return_val, int) # The return value should be an integer
assert a % return_val == 0 # The return value should be a divisor of a
assert b % return_val == 0 # The return value should be a divisor of b
assert all(a % i != 0 or b % i != 0 for i in range(return_val + 1, min(a, b))) # The return value should be the greatest common divisor of a and b
```