def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize variables to keep track of the start and end indices of each group
    start = 0
    end = 0
    
    # Loop through the characters of the paren_string
    for i in range(len(paren_string)):
        # If the current character is an opening parenthesis, update the start index
        if paren_string[i] == "(":
            start = i
        # If the current character is a closing parenthesis, update the end index
        elif paren_string[i] == ")":
            end = i
            # Add the current group to the list of groups
            groups.append(paren_string[start:end-1])
    
    # Return the list of separate groups
    return groups