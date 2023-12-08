def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2 == 0:
        raise ValueError("The list must have an even number of coefficients.")

    # Check if the largest non-zero coefficient is zero
    largest_coefficient = max(xs)
    if largest_coefficient == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")

    # Iterate over all possible values of x
    for x in range(-1000, 1000):
        # Evaluate the polynomial at the current value of x
        result = poly(xs, x)

        # Check if the result is zero
        if result == 0:
            return x

    # If no zero point is found, raise an exception
    raise ValueError("No zero point found.")