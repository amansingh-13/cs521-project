def count_distinct_characters(string: str) -> int:
    # Create an empty set to store the distinct characters
    distinct_chars = set()

    # Convert the string to lowercase to ignore the case
    string = string.lower()

    # Loop through each character in the string
    for char in string:
        # Add the character to the set if it is not already in there
        distinct_chars.add(char)

    # Return the number of distinct characters
    return len(distinct_chars)