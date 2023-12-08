def parse_nested_parens(paren_string: str) -> List[int]:
    # Initialize an empty list to store the deepest level of nesting for each group of parentheses
    levels = []
    
    # Split the input string by spaces to get each group of parentheses
    groups = paren_string.split()
    
    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current level of nesting
        level = 0
        # Initialize a variable to keep track of the maximum level of nesting
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the level of nesting
            if char == '(':
                level -= 1
                max_level = max(max_level, level)
            # If the character is a closing parenthesis, decrease the level of nesting
            elif char == ')':
                level -= 1
        
        # Append the maximum level of nesting for the current group to the levels list
        levels.append(max_level)
    
    # Return the list of maximum levels of nesting for each group of parentheses
    return levels