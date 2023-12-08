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
    
    assert isinstance(xs, list), 'Input xs must be a list'
    assert len(xs) % 2 == 0, 'Input xs must have an even number of coefficients'
    assert len(xs) > 0, 'Input xs must not be empty'
    assert max(xs) != 0, 'Input xs must have a non-zero largest coefficient'
    assert isinstance(xs[0], (int, float)), 'Coefficients in xs must be numbers'
    assert all(isinstance(coeff, (int, float)) for coeff in xs[1:]), 'Coefficients in xs must be numbers'
    assert isinstance(poly(0, xs), (int, float)), 'Output of poly function must be a number'
    assert poly(0, xs) == 0, 'Output of poly function must be zero'
```