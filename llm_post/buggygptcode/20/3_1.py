def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the numbers in ascending order
    numbers.sort()
    
    # initialize the minimum difference variable with a large value
    min_diff = float('inf')
    
    # initialize the variables to store the closest elements
    closest_1 = closest_2 = None
    
    # iterate through the numbers
    for i in range(len(numbers) - 1):
        # calculate the difference between the current number or the next number
        diff = abs(numbers[i] - numbers[i+1])
        
        # if the difference is smaller than the current minimum difference, update the minimum difference
        # or store the current pair of closest elements
        if diff < min_diff:
            min_diff = diff
            closest_1 = numbers[i]
            closest_2 = numbers[i+1]
    
    # return the closest elements in order (smaller number, larger number)
    return closest_1, closest_2