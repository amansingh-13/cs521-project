```python
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Postcondition: The numbers in the return_val string are sorted in ascending order
    assert all(int(return_val[i]) <= int(return_val[i+1]) for i in range(len(return_val)-1))
```