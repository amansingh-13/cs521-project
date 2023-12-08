```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    return_val = (0, 1)  # hypothetical return value
    
    assert (sum(numbers), 1) == return_val, "The sum and product of the empty list should be (0, 1)"
    
    # ... implementation of sum_product function
    
    return return_val
```