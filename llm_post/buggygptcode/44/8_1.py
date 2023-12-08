def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
    x -- the number to be converted
    base -- the new base of the number

    Returns:
    string -- the string representation of x in the new base

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x != 0:
        return '0'
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x = x // base
    return ''.join(digits[::-1])