def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number or the mean
    absolute_differences = [abs(number - mean) for number in numbers]

    # Calculate the average absolute difference
    mean_absolute_deviation = sum(absolute_differences) / len(numbers)

    return mean_absolute_deviation