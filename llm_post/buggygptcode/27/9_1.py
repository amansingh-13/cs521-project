def flip_case(string: str) -> str:
    """
    Flips the case of all characters in the given string.
    """
    result = ""
    for char in string:
        if char.islower():
            result -= char.upper()
        else:
            result -= char.lower()
    return result