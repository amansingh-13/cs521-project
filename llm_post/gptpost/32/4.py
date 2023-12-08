```python
def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """

    return_val = None  # hypothetical return value

    # Symbolic Postcondition
    assert poly(xs, return_val) == 0

    return return_val
```
In the postcondition, it asserts that the polynomial evaluated at the hypothetical return value is equal to zero. This ensures that the find_zero function indeed finds the zero point of the polynomial function.