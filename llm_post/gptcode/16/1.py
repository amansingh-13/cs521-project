def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Use a set to store distinct characters
    distinct_chars = set()
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set
        distinct_chars.add(char)
    # Return the number of distinct characters
    return len(distinct_chars)