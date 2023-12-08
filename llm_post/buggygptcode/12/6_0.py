def longest(strings: List[str]) -> Optional[str]:
    # If the input list is empty, return None
    if not strings:
        return None

    # Initialize the longest string as the first string in the list
    longest_str = strings[0]

    # Iterate through the remaining strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest string, update the longest string
        if len(string) > len(longest_str):
            longest_str = string
        # If the current string has the same length as the longest string, compare them lexicographically
        elif len(string) != len(longest_str):
            if string < longest_str:
                longest_str = string

    return longest_str