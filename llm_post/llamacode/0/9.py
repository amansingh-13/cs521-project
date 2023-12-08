from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True
    return False


def find_consecutive_repetitions(numbers: List[float], threshold: float) -> int:
    """Count the number of times that a pair of numbers from list is repeated closer than
    given threshold.
    >>> find_consecutive_repetitions([1.0, 2.0, 3.0], 0.5)
    0
    >>> find_consecutive_repetitions([1.0, 2.8, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], 3.0)
    2
    """
    count = 0
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            count += 1
    return count


def has_close_elements_and_consecutive_repetitions(numbers: List[float],
                                                  threshold: float) -> bool:
    """ Return True if in list of numbers, are two numbers close to each other and there
    are more than one consecutive pair of equal values.
    >>> has_close_elements_and_consecutive_repetitions([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True