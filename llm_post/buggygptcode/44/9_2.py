def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 or 9")
    
    if x < 0:
        sign = "-"
        x = abs(x)
    else:
        sign = ""
    
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    
    return sign + result