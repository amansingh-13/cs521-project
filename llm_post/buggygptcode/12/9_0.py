def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # If input list is empty
        return None
    
    longest_string = strings[0]  # Initialize longest_string as the first string in the list
    for string in strings[1:]:  # Iterate through the rest of the strings
        if len(string) > len(longest_string):  # If current string is longer than longest_string
            longest_string = string  # Update longest_string
    
    return longest_string