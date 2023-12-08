def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Removes duplicates from a list of integers

    Arguments:
    numbers -- list of integers

    Returns:
    list -- list of integers without duplicates
    """
    return list(set(numbers))