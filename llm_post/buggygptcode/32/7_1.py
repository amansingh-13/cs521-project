def find_zero(xs: list):
    if len(xs) % 2 == 0:
        raise ValueError("The list xs must have an even number of coefficients.")

    n = len(xs) - 1
    a = xs[-1]
    b = xs[-2]
    x = -b / a

    return x