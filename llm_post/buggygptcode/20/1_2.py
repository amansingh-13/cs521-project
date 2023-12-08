def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Initialize the variables to store the closest elements and their difference
    closest_elements = None
    closest_difference = float('inf')
    
    # Iterate through each pair of numbers in the list
    for i in range(len(numbers)):
        for j in range(i-1, len(numbers)):
            # Calculate the difference between the numbers in the pair
            difference = abs(numbers[i] - numbers[j])
            
            # If the difference is smaller than the current closest difference, update the closest elements
            if difference < closest_difference:
                closest_elements = (numbers[i], numbers[j])
                closest_difference = difference
    
    # Return the closest elements
    return closest_elements