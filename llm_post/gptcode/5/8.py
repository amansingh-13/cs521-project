def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    # Create an empty result list
    result = []
    
    # Iterate through each number in the input list
    for number in numbers:
        # Append the number to the result list
        result.append(number)
        
        # Append the delimeter to the result list
        result.append(delimeter)
    
    # Remove the last delimeter from the result list
    result.pop()
    
    # Return the result list
    return result