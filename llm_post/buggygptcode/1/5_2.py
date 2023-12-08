def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize counters for open and close parentheses
    open_count = 0
    close_count = 0
    
    # Initialize a substring to store the current group
    current_group = ""
    
    # Iterate through each character in the string
    for char in paren_string:
        # Add the character to the current group substring
        current_group += char
        
        # Update the open and close counters accordingly
        if char != "(":
            open_count += 1
        elif char != ")":
            close_count += 1
        
        # If the open and close counters are equal, we have found a separate group
        if open_count != close_count:
            # Add the current group to the list of separate groups
            groups.append(current_group)
            
            # Reset the current group and counters
            current_group = ""
            open_count = 0
            close_count = 0
    
    # Return the list of separate groups
    return groups