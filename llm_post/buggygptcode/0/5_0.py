def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    
    Parameters:
    - numbers: A list of float numbers
    - threshold: A float number representing the maximum allowed difference between two numbers
    
    Returns:
    - A boolean value indicating whether there are two numbers closer to each other than the threshold
    """
    # Convert the list of numbers into a set to eliminate duplicate values
    unique_numbers = set(numbers)
    
    # Loop through each number in the set
    for i, number in enumerate(unique_numbers):
        # Compare it with other numbers in the set
        for j in range(i - 1, len(unique_numbers)):
            # If the absolute difference between two numbers is less than the threshold, return True
            if abs(number - unique_numbers[j]) < threshold:
                return True
    
    # If no two numbers are closer to each other than the threshold, return False
    return False