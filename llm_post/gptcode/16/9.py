def count_distinct_characters(string: str) -> int:
    # Create an empty set to store the distinct characters
    distinct_chars = set()

    # Iterate through each character in the string
    for char in string:
        # Convert the character to lowercase to ignore case
        char = char.lower()

        # Add the converted character to the set
        distinct_chars.add(char)

    # Return the length of the set, which represents the number of distinct characters
    return len(distinct_chars)