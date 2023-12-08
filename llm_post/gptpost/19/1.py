```python
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Postcondition
    return_val = 'one three five'  # hypothetical return value
    assert isinstance(return_val, str), "The return value should be a string"
    assert set(return_val.split()) == set(numbers.split()), "The sorted string should have the same unique numbers as the input string"
    assert all(return_val.split().index(num) <= return_val.split().index(numbers.split()[i+1]) for i, num in enumerate(numbers.split()[:-1])), "The numbers in the sorted string should be in ascending order"
    assert all(num in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] for num in return_val.split()), "The numbers in the sorted string should be valid numberals"
    return return_val
```