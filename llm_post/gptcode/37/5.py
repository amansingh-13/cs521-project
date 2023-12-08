def sort_even(l: list):
    # Create a new list to store the sorted values at even indices
    sorted_values = sorted(l[::2])
    
    # Create a new list to store the result
    result = []
    
    # Iterate through the original list and append the values to the result list
    # If the index is even, append the sorted value from the sorted_values list
    # If the index is odd, append the value from the original list
    for i, value in enumerate(l):
        if i % 2 == 0:
            result.append(sorted_values.pop(0))
        else:
            result.append(value)
    
    return result