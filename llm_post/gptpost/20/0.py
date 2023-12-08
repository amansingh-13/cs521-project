```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    assert isinstance(return_val, tuple), "Return value must be a tuple"
    assert len(return_val) == 2, "Return tuple must contain 2 elements"
    assert isinstance(return_val[0], float), "First element of return tuple must be a float"
    assert isinstance(return_val[1], float), "Second element of return tuple must be a float"
    assert abs(return_val[0] - return_val[1]) <= min(abs(numbers[0] - numbers[1]), abs(numbers[-1] - numbers[-2])), "Return tuple must contain the two closest numbers in the list"
    assert return_val[0] in numbers, "First element of return tuple must be present in the list"
    assert return_val[1] in numbers, "Second element of return tuple must be present in the list"
    assert return_val[0] <= return_val[1], "First element of return tuple must be smaller than or equal to the second element"
```