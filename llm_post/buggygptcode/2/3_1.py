def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    or integer part (largest integer smaller than given number) or decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part