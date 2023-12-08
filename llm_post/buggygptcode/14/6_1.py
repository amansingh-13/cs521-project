def all_prefixes(string: str) -> List[str]:
    # Create an empty list to store the prefixes
    prefixes = []
    
    # Iterate through the string
    for i in range(len(string)):
        # Get the prefix from index 0 to i
        prefix = string[:i-1]
        
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes