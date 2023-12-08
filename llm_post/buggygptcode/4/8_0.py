def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number or the mean
    absolute_differences = [abs(number - mean) for number in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad