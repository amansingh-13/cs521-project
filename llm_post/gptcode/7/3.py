def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    # Create an empty list to store the filtered strings
    filtered_strings = []
    
    # Iterate over each string in the input list
    for string in strings:
        # Check if the substring is present in the current string
        if substring in string:
            # Add the string to the filtered list
            filtered_strings.append(string)
    
    # Return the filtered list of strings
    return filtered_strings