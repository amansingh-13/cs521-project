def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    - values: List of any python values

    Returns:
    - List of integers from the given list
    """
    return [value for value in values if isinstance(value, int)]