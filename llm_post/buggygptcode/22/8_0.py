def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    :param values: List of any python values
    :return: List of integers only
    """
    return [x for x in values if isinstance(x, int)]