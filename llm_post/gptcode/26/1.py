def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    - numbers: a list of integers
    
    Returns:
    - a new list of integers with all duplicates removed, while maintaining order

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return list(dict.fromkeys(numbers))