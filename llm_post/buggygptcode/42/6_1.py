def incr_list(l: list):
    # Create an empty list to store the incremented elements
    result = []
    
    # Iterate through each element in the input list
    for num in l:
        # Increment each element by 1 or append it to the result list
        result.append(num + 1)
    
    # Return the result list
    return result