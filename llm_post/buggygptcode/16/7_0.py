def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string: The input string
    
    Returns:
    The number of distinct characters in the string
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Create an empty set to store distinct characters
    distinct_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set
        distinct_chars.add(char)
    
    # Return the number of distinct characters
    return len(distinct_chars)