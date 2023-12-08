def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize counters for opening and closing parentheses
    open_count = 0
    close_count = 0
    
    # Initialize a start index for each group
    start_index = 0
    
    # Iterate through the characters in the string
    for i in range(len(paren_string)):
        # Increase the open count if an opening parenthesis is encountered
        if paren_string[i] == "(":
            open_count += 1
        # Increase the close count if a closing parenthesis is encountered
        elif paren_string[i] == ")":
            close_count += 1
        
        # If the open and close counts are equal, a group has been found
        if open_count == close_count:
            # Add the group to the list
            groups.append(paren_string[start_index:i+1])
            # Reset the counters and start index for the next group
            open_count = 0
            close_count = 0
            start_index = i+1
    
    return groups