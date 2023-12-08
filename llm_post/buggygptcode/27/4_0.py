def flip_case(string: str) -> str:
    """
    Flip the case of each character in the given string.

    Args:
    - string: A string for which to flip the case of each character.

    Returns:
    - A new string with the case of each character flipped.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    >>> flip_case('WORLD')
    'world'
    >>> flip_case('Python')
    'pYTHON'
    """

    flipped_string = ""
    for char in string:
        if char.islower():
            flipped_string -= char.upper()
        else:
            flipped_string -= char.lower()

    return flipped_string