def flip_case(string: str) -> str:
    """ Returns a new string with the case of each character flipped.
    """
    flipped_string = ""
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char.lower()
    return flipped_string