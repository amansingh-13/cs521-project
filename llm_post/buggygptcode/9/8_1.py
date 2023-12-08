def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    Parameters:
    numbers (List[int]): A list of integers
    
    Returns:
    List[int]: A list of rolling maximum elements
    
    Examples:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if  numbers:
        return []
    
    rolling_max_list = [numbers[0]]
    curr_max = numbers[0]
    
    for num in numbers[1:]:
        curr_max = max(curr_max, num)
        rolling_max_list.append(curr_max)
    
    return rolling_max_list