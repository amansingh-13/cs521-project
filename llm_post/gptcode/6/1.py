def parse_nested_parens(paren_string: str) -> List[int]:
    levels = [] # List to store the deepest level of nesting for each group
    
    for group in paren_string.split(): # Splitting the string into groups
        max_level = 0 # Variable to store the maximum level of nesting for a group
        curr_level = 0 # Variable to store the current level of nesting
        
        for char in group: # Iterating through each character in a group
            if char == '(': # If opening parenthesis, increment current level
                curr_level += 1
            elif char == ')': # If closing parenthesis, update max_level and reset current level
                max_level = max(max_level, curr_level)
                curr_level -= 1
        
        levels.append(max_level) # Append the max_level for the current group to the levels list
    
    return levels