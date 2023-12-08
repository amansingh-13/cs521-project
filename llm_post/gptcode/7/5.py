def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    :param strings: Input list of strings
    :param substring: Substring to search for
    :return: List of strings that contain the given substring
    """
    return [s for s in strings if substring in s]