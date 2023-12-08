```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # Postcondition: For any even index i in l, the value at that index in return_val is equal to the sorted values of even indices in l.
    assert all(return_val[i] == sorted([l[j] for j in range(len(l)) if j % 2 == 0]) for i in range(len(return_val)) if i % 2 == 0)
```