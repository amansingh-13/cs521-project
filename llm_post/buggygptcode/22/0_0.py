def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    return [x for x in values if isinstance(x, int)]