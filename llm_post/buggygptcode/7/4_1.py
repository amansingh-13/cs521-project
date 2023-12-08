def filter_by_substring(strings, substring):
    """
    This function filters an input list of strings and keeps only the ones that contain
    the given substring.

    Args:
    strings (List[str]): The input list of strings.
    substring (str): The substring to filter by.

    Returns:
    List[str]: The filtered list of strings.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]