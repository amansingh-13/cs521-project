```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    assert isinstance(return_val, Tuple[int, int]), "Return value must be a tuple of two integers"
    assert len(return_val) == 2, "Return value must contain two elements"
    assert isinstance(return_val[0], int) and isinstance(return_val[1], int), "Elements of the tuple must be integers"
    assert return_val[0] == sum(numbers) if numbers else 0, "Sum must be equal to the sum of the numbers or 0 if numbers is empty"
    assert return_val[1] == math.prod(numbers) if numbers else 1, "Product must be equal to the product of the numbers or 1 if numbers is empty"
```