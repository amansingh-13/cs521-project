def filter_integers(values: List[Any]) -> List[int]:
    """
    This function takes a list of any python values or returns a new list containing only the integers from the original list.
    """
    return [value for value in values if isinstance(value, int)]