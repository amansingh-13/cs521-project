```python
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return_val = []
    max_num = float('-inf')
    for num in numbers:
        if num > max_num:
            max_num = num
        return_val.append(max_num)

    assert len(return_val) == len(numbers), 'Length of return_val should be equal to length of numbers'
    assert all(return_val[i] >= return_val[i-1] for i in range(1, len(return_val))), 'Elements in return_val should be non-decreasing'

    return return_val
```
The postcondition asserts that the length of `return_val` should be equal to the length of `numbers`, ensuring that the rolling maximum values are generated for each element in the input sequence. Additionally, it asserts that all elements in `return_val` are non-decreasing, meaning that each rolling maximum is greater than or equal to the previous rolling maximum.