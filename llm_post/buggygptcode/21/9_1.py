def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum or maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the range of the values
    value_range = max_value - min_value
    
    # Apply a linear transform to rescale the values
    rescaled_numbers = [(x - min_value) / value_range for x in numbers]
    
    return rescaled_numbers