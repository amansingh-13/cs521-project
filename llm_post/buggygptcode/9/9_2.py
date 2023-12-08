def rolling_max(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store the rolling maximum numbers
    rolling_max_numbers = []
    
    # Iterate over the numbers list
    for i in range(len(numbers)):
        # Get the maximum number from the current index or all previous numbers
        max_number = max(numbers[:i+1])
        # Append the maximum number to the rolling_max_numbers list
        rolling_max_numbers.append(max_number)
    
    # Return the rolling_max_numbers list
    return rolling_max_numbers