from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[j] - numbers[i]) <= threshold:
                return True
    return False


def close_elements(numbers: List[float], threshold: float) -> bool:
    """ Find the index of two elements in given list of numbers that are closer to each other than
    given threshold.
    >>> close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    2
    """
    if len(numbers) < 2:
        raise ValueError('At least two numbers are required')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[j] - numbers[i]) <= threshold:
                return f'{i} and {j}'
    return False


if __name__ == '__main__':
