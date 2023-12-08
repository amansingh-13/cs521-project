def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element or the mean
    absolute_differences = [abs(x - mean) for x in numbers]
    
    # Calculate the average absolute difference
    mad = sum(absolute_differences) / len(numbers)
    
    return mad