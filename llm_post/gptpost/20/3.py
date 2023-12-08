```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Postcondition:
    assert isinstance(return_val, tuple), "The return value should be a tuple."
    assert len(return_val) == 2, "The tuple should contain exactly two elements."
    assert return_val[0] in numbers, "The first element of the tuple should be one of the input numbers."
    assert return_val[1] in numbers, "The second element of the tuple should be one of the input numbers."
    assert abs(numbers.index(return_val[0]) - numbers.index(return_val[1])) == 1, "The two elements should be adjacent in the original list."
    assert return_val[0] <= return_val[1], "The first element of the tuple should be smaller than or equal to the second element."
```