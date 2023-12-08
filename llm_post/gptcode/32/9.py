def find_zero(xs):
    if len(xs) % 2 != 0:
        raise ValueError("The list xs must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    max_coeff = max(xs, key=abs)
    
    if max_coeff == 0:
        raise ValueError("The list xs must have a largest non-zero coefficient")
    
    # Find the index of the largest non-zero coefficient
    max_index = xs.index(max_coeff)
    
    # Divide the list into two parts
    xs1 = xs[:max_index+1]
    xs2 = xs[max_index+1:]
    
    # Find the zero of the polynomial using the bisection method
    a = -1
    b = 1
    while abs(b - a) >= 1e-10:
        c = (a + b) / 2
        if poly(xs1, c) * poly(xs2, c) <= 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2