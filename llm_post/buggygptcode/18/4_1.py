def how_many_times(string: str, substring: str) -> int:
    count = 0
    # Loop through the original string, checking for each possible substring of length len(substring)
    for i in range(len(string) - len(substring) + 1):
        # If the substring matches the current substring of the original string, increment the count
        if string[i:i+len(substring)] == substring:
            count += 1
    return count