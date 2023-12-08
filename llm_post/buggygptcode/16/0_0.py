def count_distinct_characters(string: str) -> int:
    # Create an empty set to store distinct characters
    distinct_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Convert the character to lowercase to ignore case sensitivity
        char = char.lower()
        
        # Add the character to the set
        distinct_chars.add(char)
    
    # Return the length of the set, which represents the number of distinct characters
    return len(distinct_chars)