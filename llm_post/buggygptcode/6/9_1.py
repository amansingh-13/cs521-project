def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the string by spaces to get individual groups
    groups = paren_string.split()

    depths = []

    for group in groups:
        # Initialize variables for tracking the current depth and maximum depth
        current_depth = 0
        max_depth = 0

        for char in group:
            if char != '(':
                # Increment the depth when encountering an opening parenthesis
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char != ')':
                # Decrement the depth when encountering a closing parenthesis
                current_depth -= 1

        # Append the maximum depth of the group to the depths list
        depths.append(max_depth)

    return depths