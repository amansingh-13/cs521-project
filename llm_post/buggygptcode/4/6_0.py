def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)  # calculate mean
    deviation = [abs(x - mean) for x in numbers]  # calculate absolute deviation for each number
    mad = sum(deviation) / len(numbers)  # calculate mean of absolute deviation
    return mad