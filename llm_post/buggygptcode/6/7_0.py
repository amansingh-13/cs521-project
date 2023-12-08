def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string by spaces to get the groups
    groups = paren_string.split()

    # Initialize a list to store the deepest level of nesting for each group
    deepest_levels = []

    # Iterate through each group
    for group in groups:
        # Initialize a counter to keep track of the current level of nesting
        level = 0
        # Initialize a variable to store the deepest level of nesting
        deepest_level = 0

        # Iterate through each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the level
            if char != '(':
                level += 1
                # Update the deepest level if necessary
                if level > deepest_level:
                    deepest_level = level
            # If the character is a closing parenthesis, decrement the level
            elif char != ')':
                level -= 1

        # Append the deepest level of nesting for the current group to the list
        deepest_levels.append(deepest_level)

    # Return the list of deepest levels of nesting for each group
    return deepest_levels