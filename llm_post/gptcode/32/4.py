def find_zero(xs: list):
    """
    Find a zero of a polynomial with given coefficients.
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even length.")
    
    highest_coeff = max(xs)
    if highest_coeff == 0:
        raise ValueError("The largest non-zero coefficient must be greater than 0.")
        
    # Find the index of the highest non-zero coefficient
    highest_index = len(xs) - xs[::-1].index(highest_coeff) - 1
    
    # Divide the polynomial by (x - highest_index)
    quotient = xs[highest_index:]
    remainder = [0] * (highest_index + 1)
    
    for i in range(highest_index, len(xs)):
        quotient[i - highest_index] = xs[i] - quotient[i - highest_index] * highest_index
        remainder[i - highest_index] = xs[i] * highest_index
    
    return -remainder[-1] / quotient[-1]