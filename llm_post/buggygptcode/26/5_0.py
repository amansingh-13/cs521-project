def remove_duplicates(numbers: List[int]) -> List[int]:
    # Create an empty set to keep track of unique numbers
    unique_numbers = set()
    # Create a new list to store the unique numbers in the original order
    result = []
    
    # Iterate through the numbers
    for num in numbers:
        # Check if the number is  already in the set
        if num  in unique_numbers:
            # Add the number to the set
            unique_numbers.add(num)
            # Add the number to the result list
            result.append(num)
    
    return result