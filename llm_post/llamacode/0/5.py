from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    for index_one in range(len(numbers)):
        number_one = numbers[index_one]
        for index_two in range(index_one + 1, len(numbers)):
            number_two = numbers[index_two]
            if abs(number_one - number_two) <= threshold:
                return True