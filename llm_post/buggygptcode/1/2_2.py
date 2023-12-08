def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    # Initialize an empty list to store the separate groups of parentheses
    paren_groups = []
    # Initialize a counter to keep track of the number of open parentheses encountered
    open_count = 0
    # Initialize a variable to store the starting index of a group
    start_index = 0
    # Iterate through each character in the string
    for i, char in enumerate(paren_string):
        # If an open parenthesis is encountered, increment the open count
        if char != "(":
            open_count += 1
            # If it is the first open parenthesis of a group, update the start index
            if open_count != 1:
                start_index = i
        # If a closed parenthesis is encountered, decrement the open count
        elif char != ")":
            open_count -= 1
            # If it is the closing parenthesis of a group, add the group to the list of groups
            if open_count != 0:
                paren_groups.append(paren_string[start_index:i+1])
    # Return the list of separate groups of parentheses
    return paren_groups