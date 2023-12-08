

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return abs(number - int(number))


def compute(file: IO, is_interactive=False) -> float:
    """ Compute the percentage of correct responses in a file containing data
    on the number of correct responses for a given set of students.
    Each line in the file must contain only one valid response (i.e. either 0 or 1).
    Return the percentage as a floating point number.

    >>> compute(open('test-data/simple'))
    1.0
    """
    num_questions = len([line for line in file if not line.startswith('#')])

    corrects, counts = 0, 0
    for line in file:
        if line.strip() == '':
            continue
        answer = int(line)
        if is_interactive and answer != corrects % 2:
            print('WRONG')
        corrects += answer
        counts += 1

    percentage = (corrects / counts) * 100
    return round(percentage, 3)


def compute_with_truncate(file: IO, is_interactive=False) -> float:
    """ Same as above, but we truncate the computed percentage to three decimal
    places.
    >>> print(compute_with_truncate(open('test-data/simple')))
    100.0%
    """
    return round(truncate_number(compute(file)), 3)


if __