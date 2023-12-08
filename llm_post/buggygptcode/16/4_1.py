def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Create an empty set to store distinct characters
    distinct_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is already in the set
        if char  in distinct_chars:
            # If , add it to the set
            distinct_chars.add(char)
    
    # Return the size of the set, which is the number of distinct characters
    return len(distinct_chars)