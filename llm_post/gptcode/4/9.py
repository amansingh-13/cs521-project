def mean_absolute_deviation(numbers: List[float]) -> float:
    n = len(numbers)
    mean = sum(numbers) / n
    deviation = [abs(x - mean) for x in numbers]
    mad = sum(deviation) / n
    return mad