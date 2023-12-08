```python
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    assert isinstance(return_val, str), 'Return value is not a string'
    assert isinstance(numbers, str), 'Input is not a string'
    assert isinstance(return_val.split(), list), 'Return value is not a list'
    assert isinstance(numbers.split(), list), 'Input is not a list'
    assert all(num in {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'} for num in numbers.split()), 'Invalid number in the input'
    assert all(num in {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'} for num in return_val.split()), 'Invalid number in the return value'
    assert sorted(numbers.split()) == return_val.split(), 'Numbers are not sorted correctly'
```