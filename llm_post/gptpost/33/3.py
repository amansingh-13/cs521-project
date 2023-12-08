```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

# Symbolic Postcondition:
assert all((l[i] == return_val[i] for i in range(len(l)) if i % 3 != 0)) and \
       all((sorted(l[i:i+3]) == sorted(return_val[i:i+3]) for i in range(0, len(l), 3)))
```