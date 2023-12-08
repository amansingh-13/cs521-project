def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to treat characters regardless of case
    string = string.lower()

    # Use a set to store distinct characters
    distinct_chars = set(string)

    # Return the length of the set
    return len(distinct_chars)