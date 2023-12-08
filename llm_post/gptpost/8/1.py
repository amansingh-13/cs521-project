```python
# Postcondition for sum_product function
assert isinstance(return_val, tuple), "Return value should be a tuple"
assert len(return_val) == 2, "Return value tuple should contain two elements"

sum_val = return_val[0]
prod_val = return_val[1]

assert isinstance(sum_val, int), "Sum value should be an integer"
assert isinstance(prod_val, int), "Product value should be an integer"

# Check if sum and product are calculated correctly
if len(numbers) == 0:
    assert sum_val == 0, "Empty sum should be equal to 0"
    assert prod_val == 1, "Empty product should be equal to 1"
else:
    calculated_sum = sum(numbers)
    calculated_prod = 1
    for num in numbers:
        calculated_prod *= num
    assert sum_val == calculated_sum, "Sum should be calculated correctly"
    assert prod_val == calculated_prod, "Product should be calculated correctly"
```