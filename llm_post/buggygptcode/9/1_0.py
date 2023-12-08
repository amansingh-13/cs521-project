def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    """
    rolling_max_list = []
    max_num = None

    for num in numbers:
        if max_num is None or num > max_num:
            max_num = num
        rolling_max_list.append(max_num)

    return rolling_max_list