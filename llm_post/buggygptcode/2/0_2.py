def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    # Convert the number to a string
    number_str = str(number)

    # Find the position of the decimal point
    decimal_point_index = number_str.index('.')

    # Extract the decimal part of the number
    decimal_part = number_str[decimal_point_index+1:]

    # Convert the decimal part back to a float
    decimal_part_float = float('0.' + decimal_part)

    return decimal_part_float