def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence. """
    
    # Initialize an empty list to store the rolling maximums
    rolling_max_numbers = []
    
    # Iterate through the numbers list
    for i in range(len(numbers)):
        # Find the maximum number in the current sublist (from the start to the current index)
        max_number = max(numbers[:i+1])
        # Append the maximum number to the rolling_max_numbers list
        rolling_max_numbers.append(max_number)
    
    # Return the rolling_max_numbers list
    return rolling_max_numbers