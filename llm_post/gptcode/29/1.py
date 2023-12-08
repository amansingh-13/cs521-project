def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Parameters:
    strings (List[str]): List of strings to filter
    prefix (str): Prefix string to filter by

    Returns:
    List[str]: List of strings that start with the given prefix
    """

    return [s for s in strings if s.startswith(prefix)]