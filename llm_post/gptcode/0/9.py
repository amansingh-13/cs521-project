def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate through the list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if abs(numbers[i] - numbers[i+1]) < threshold:
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False