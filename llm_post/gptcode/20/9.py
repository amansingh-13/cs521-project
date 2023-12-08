def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Initialize the variables to store the closest elements
    closest_elements = (numbers[0], numbers[1])
    min_diff = abs(numbers[0] - numbers[1])
    
    # Iterate through the sorted list and compare the difference between adjacent elements
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        
        # If the difference is smaller than the current minimum difference, update the closest elements
        if diff < min_diff:
            min_diff = diff
            closest_elements = (numbers[i], numbers[i+1])
    
    return closest_elements