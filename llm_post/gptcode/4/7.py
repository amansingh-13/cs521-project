def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the mean absolute deviation of a list of numbers.

    Args:
    - numbers: A list of floating-point numbers.

    Returns:
    - The mean absolute deviation of the numbers.

    """

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the average of the absolute differences
    mean_absolute_deviation = sum(absolute_diffs) / len(numbers)

    return mean_absolute_deviation