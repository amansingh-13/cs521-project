def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a or b """
    while b != 0:
        a, b = b, a % b
    return a