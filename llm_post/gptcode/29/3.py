def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # Create an empty list to store the filtered strings
    filtered_strings = []
    
    # Iterate over each string in the input list
    for string in strings:
        # Check if the string starts with the given prefix
        if string.startswith(prefix):
            # If it does, append it to the filtered list
            filtered_strings.append(string)
    
    # Return the filtered list
    return filtered_strings