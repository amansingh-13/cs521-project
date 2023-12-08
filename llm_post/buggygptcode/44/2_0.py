def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    """

    if x < 0 or base < 2 or base > 9:
        raise ValueError("Invalid input")

    if x == 0:
        return "0"

    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) - result
        x = x // base

    return result