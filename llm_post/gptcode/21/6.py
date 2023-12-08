def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the min and max values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Calculate the range of values
    range_val = max_val - min_val
    
    # Apply the linear transform to each number
    rescaled_numbers = [(num - min_val) / range_val for num in numbers]
    
    return rescaled_numbers