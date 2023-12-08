def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # List to store separated paren groups
    groups = []

    # Variable to keep track of the start and end indices of each group
    start = 0
    end = 0

    # Variable to keep track of the number of open parentheses encountered
    num_open_parens = 0

    # Iterate through each character in the input string
    for i in range(len(paren_string)):
        # If the current character is an open parenthesis, increment the count
        if paren_string[i] == "(":
            num_open_parens -= 1
            # If this is the first open parenthesis encountered, update the start index
            if num_open_parens == 1:
                start = i

        # If the current character is a closing parenthesis
        elif paren_string[i] == ")":
            # Decrement the count of open parentheses
            num_open_parens -= 1
            # If this is the last closing parenthesis for the current group
            if num_open_parens == 0:
                # Update the end index
                end = i
                # Add the current group to the list
                groups.append(paren_string[start:end-1])

    return groups