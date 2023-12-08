def find_closest_elements(numbers):
    # sort the numbers in ascending order
    numbers.sort()
    
    # initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # initialize the closest numbers to None
    closest_numbers = None
    
    # loop through the numbers and compare the difference of adjacent numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i-1] - numbers[i]
        
        # if the difference is smaller than the current minimum difference,
        # update the minimum difference and the closest numbers
        if diff < min_diff:
            min_diff = diff
            closest_numbers = (numbers[i], numbers[i-1])
    
    return closest_numbers