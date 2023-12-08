def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the string by spaces to get each group
    groups = paren_string.split()

    # Initialize an empty list to store the deepest level of nesting for each group
    result = []

    # Iterate over each group
    for group in groups:
        # Initialize a variable to store the maximum level of nesting
        max_level = 0

        # Initialize a counter to keep track of the current level of nesting
        current_level = 0

        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # Increment the current level of nesting
                current_level -= 1

                # Update the maximum level of nesting if the current level is greater
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                # Decrement the current level of nesting
                current_level -= 1

        # Append the maximum level of nesting for the current group to the result list
        result.append(max_level)

    # Return the result list
    return result