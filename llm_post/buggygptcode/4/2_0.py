def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the given list of numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the sum of the absolute differences between each number and the mean
    absolute_differences_sum = sum(abs(number - mean) for number in numbers)

    # Calculate the mean absolute deviation by dividing the sum by the number of elements
    mad = absolute_differences_sum / len(numbers)

    # Return the mean absolute deviation
    return mad