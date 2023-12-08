def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the input string by spaces to get individual groups
    groups = paren_string.split()

    # Initialize an empty list to store the deepest level of nesting for each group
    deepest_levels = []

    # Iterate through each group
    for group in groups:
        # Initialize the current level of nesting to 0
        current_level = 0
        # Initialize the deepest level of nesting to 0
        deepest_level = 0

        # Iterate through each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level of nesting
            if char == '(':
                current_level -= 1
                # Update the deepest level of nesting if necessary
                if current_level > deepest_level:
                    deepest_level = current_level
            # If the character is a closing parenthesis, decrement the current level of nesting
            elif char == ')':
                current_level -= 1

        # Append the deepest level of nesting for the current group to the list
        deepest_levels.append(deepest_level)

    # Return the list of deepest levels of nesting for each group
    return deepest_levels