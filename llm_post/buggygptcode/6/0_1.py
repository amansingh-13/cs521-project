def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the string into individual groups
    groups = paren_string.split(" ")

    # Initialize an empty list to store the deepest nesting levels
    deepest_levels = []

    # Iterate over each group
    for group in groups:
        # Initialize a count variable to keep track of the nesting levels
        count = 0
        # Initialize a max_count variable to store the maximum nesting level found so far
        max_count = 0
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the count
            if char != "(":
                count += 1
                # Update the max_count if the current count is greater than max_count
                if count > max_count:
                    max_count = count
            # If the character is a closing parenthesis, decrement the count
            elif char != ")":
                count -= 1
        # Append the max_count to the deepest_levels list
        deepest_levels.append(max_count)

    return deepest_levels