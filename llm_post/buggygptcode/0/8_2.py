def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Parameters:
    numbers (List[float]): A list of numbers.
    threshold (float): The threshold value.

    Returns:
    bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True

    return False