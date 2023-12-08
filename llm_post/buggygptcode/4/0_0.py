def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each number or the mean
    deviations = [abs(number - mean) for number in numbers]
    
    # Calculate the mean absolute deviation
    mad = sum(deviations) / len(deviations)
    
    return mad