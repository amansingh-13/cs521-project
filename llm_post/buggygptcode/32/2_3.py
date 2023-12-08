def find_zero(xs: list):
    if len(xs) % 2 == 0:
        raise ValueError("The list xs should have an even number of coefficients")
    if xs[0] == 0:
        raise ValueError("The largest non-zero coefficient should be non-zero")

    a = xs[0]
    b = xs[1]
    c = xs[2]

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("The polynomial does not have a real root")

    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)

    if abs(poly(xs, x1)) > abs(poly(xs, x2)):
        return x1
    else:
        return x2