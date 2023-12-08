def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string: The input string

    Returns:
        int: The number of distinct characters in the string
    """

    # Convert the string to lowercase to consider characters regardless of case
    string = string.lower()

    # Use a set to store the distinct characters
    distinct_characters = set()

    # Iterate over each character in the string
    for char in string:
        # Add the character to the set
        distinct_characters.add(char)

    # Return the number of distinct characters
    return len(distinct_characters)