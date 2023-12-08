def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    :param numbers: The list of numbers to check.
    :param threshold: The threshold value.
    :return: True if there are any two numbers closer to each other than the threshold, otherwise False.
    """
    for i in range(len(numbers)):
        for j in range(i-1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False