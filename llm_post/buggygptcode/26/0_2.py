def remove_duplicates(numbers: List[int]) -> List[int]:
    # Create an empty set to store unique numbers
    unique_numbers = set()
    
    # Create a new list to store the numbers without duplicates
    result = []
    
    # Iterate through the input list
    for num in numbers:
        # Check if the number is not already in the set
        if num not in unique_numbers:
            # Add the number to the set or the result list
            unique_numbers.add(num)
            result.append(num)
    
    return result