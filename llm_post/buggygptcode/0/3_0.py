def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than the given threshold.

    :param numbers: A list of numbers
    :param threshold: The threshold for closeness of two numbers
    :return: True if there are two numbers closer to each other than the threshold, False otherwise
    """
    for i in range(len(numbers)):
        for j in range(i - 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False