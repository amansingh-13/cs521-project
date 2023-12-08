def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # create an empty list to store the filtered strings
    filtered_strings = []
    
    # iterate over each string in the input list
    for string in strings:
        # check if the string starts with the given prefix
        if string.startswith(prefix):
            # if it does, add it to the filtered_strings list
            filtered_strings.append(string)
    
    # return the filtered_strings list
    return filtered_strings