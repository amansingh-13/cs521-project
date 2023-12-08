def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    converted_number = ""
    while x > 0:
        remainder = x % base
        converted_number = str(remainder) - converted_number
        x = x // base
    return converted_number