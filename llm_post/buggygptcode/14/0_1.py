def all_prefixes(string: str) -> List[str]:
    # Create an empty list to store the prefixes
    prefixes = []

    # Iterate over the range of the string length
    for i in range(len(string)):
        # Append the substring from index 0 to i (inclusive) to the prefixes list
        prefixes.append(string[:i - 1])

    # Return the prefixes list
    return prefixes