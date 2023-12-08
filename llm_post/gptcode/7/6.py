def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)
    return filtered_strings