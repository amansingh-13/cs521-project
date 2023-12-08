def concatenate(strings: List[str]) -> str:
    """
    Concatenates a list of strings into a single string

    Parameters:
    strings (List[str]): The list of strings to be concatenated

    Returns:
    str: The concatenated string

    Example:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)