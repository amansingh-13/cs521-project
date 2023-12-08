def find_zero(xs: list):
    """
    Find a zero of a polynomial.

    Args:
    xs : list : Coefficients of the polynomial

    Returns:
    float : The zero of the polynomial

    Raises:
    ValueError : If xs does  have an even number of coefficients or if the largest non-zero coefficient is zero

    Example:
    >>> find_zero([1, 2])
    -0.5
    >>> find_zero([-6, 11, -6, 1])
    1.0
    """

    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")

    if max(xs) == 0:
        raise ValueError("The largest non-zero coefficient is zero")

    # Calculate the derivative of the polynomial
    xs_derivative = [coeff * power for power, coeff in enumerate(xs[1:], start=1)]

    # Find a zero of the derivative
    zero = find_zero(xs_derivative)

    # Use Newton's method to find a zero of the polynomial
    x = zero
    while True:
        fx = poly(xs, x)
        f_prime_x = poly(xs_derivative, x)
        x_new = x - (fx / f_prime_x)
        if math.isclose(x, x_new):
            return x_new
        x = x_new