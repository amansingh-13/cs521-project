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
    if len(xs) % 2 == 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("The list of coefficients must have a non-zero maximum coefficient.")
    
    n = len(xs) - 1
    x = 0
    for i in range(n // 2):
        x += (-xs[i * 2 + 1] + math.sqrt(xs[i * 2 + 1] ** 2 - 4 * xs[i * 2] * xs[i * 2 + 2])) / (2 * xs[i * 2])
        
    return x