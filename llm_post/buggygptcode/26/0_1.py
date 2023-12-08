def remove_duplicates(numbers: List[int]) -> List[int]:
    # Create an empty set to store unique numbers
    unique_numbers = set()
    
    # Create a new list to store the numbers without duplicates
    result = []
    
    # Iterate through the input list
    for num in numbers:
        # Check if the number is  already in the set
        if num  in unique_numbers:
            # Add the number to the set and the result list
            unique_numbers.add(num)
            result.append(num)
    
    return result