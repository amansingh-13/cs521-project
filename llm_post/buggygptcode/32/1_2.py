def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    or largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2 == 1:
        raise ValueError("The number of coefficients must be even")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero")
    
    # Use the numpy library to solve the polynomial equation
    import numpy as np
    
    # Create the polynomial equation
    equation = np.poly1d(xs)
    
    # Use the roots() function to find the roots of the equation
    roots = np.roots(equation)
    
    # Return the first root
    return roots[0]