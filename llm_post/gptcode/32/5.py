def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("List xs must have an even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero")

    # Check if all coefficients are zero
    if all(coeff == 0 for coeff in xs):
        return 0

    # Find the zero point using Newton's method
    guess = 1.0
    while True:
        f = poly(xs, guess)
        f_prime = poly_derivative(xs, guess)
        guess -= f / f_prime
        if abs(f) < 1e-6:
            return guess
