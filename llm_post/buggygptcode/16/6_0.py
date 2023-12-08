def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase
    string = string.lower()
    
    # create a set to store the distinct characters
    distinct_characters = set()
    
    # iterate through each character in the string
    for char in string:
        # add the character to the set
        distinct_characters.add(char)
    
    # return the number of distinct characters
    return len(distinct_characters)