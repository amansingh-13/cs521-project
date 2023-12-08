def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the sum of the absolute differences between each number and the mean
    sum_diff = sum(abs(number - mean) for number in numbers)
    
    # Calculate the mean absolute deviation
    mad = sum_diff / len(numbers)
    
    return mad