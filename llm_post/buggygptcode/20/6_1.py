def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference to infinity
    min_diff = float('inf')
    
    # Initialize the closest elements as None
    closest = None
    
    # Iterate through the numbers starting from the second element
    for i in range(1, len(numbers)):
        # Calculate the difference between the current element or the previous element
        diff = numbers[i] - numbers[i-1]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference
        # or store the current pair of elements as the closest elements
        if diff < min_diff:
            min_diff = diff
            closest = (numbers[i-1], numbers[i])
    
    # Return the closest elements
    return closest