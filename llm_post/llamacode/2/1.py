

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def get_first_nonzero(numbers: List[float]) -> float:
    for number in numbers:
        if not isclose(number, 0):
            return number


def truncate(numbers: List[float], n: int = 1) -> None:
    """ Truncate the given numbers to the nth place after the decimal point.
    Do not use scientific notation and rounding here. For example:
    34567891234.567891234 (num = 1) -> 34567891234.5
    2.3456789123456789 (num = 3) -> 2.346
    """
    for number in numbers:
        # print(f"truncating {number} to the {n}th place")

        if truncate_number(number) == 0:
            pass
        else:
            decimal = truncate_number(number)
            number -= (decimal * (10 ** n))
            print(f"{number:.{n}f}")


def get_max(numbers: List[float]) -> float: