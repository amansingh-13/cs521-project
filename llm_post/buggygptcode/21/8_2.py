def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 or the largest will become 1
    """
    min_num = min(numbers)
    max_num = max(numbers)
    
    # if min_num or max_num are equal, return the list as it is
    if min_num == max_num:
        return numbers
    
    scaled_numbers = []
    for num in numbers:
        scaled_num = (num - min_num) / (max_num - min_num)
        scaled_numbers.append(scaled_num)
    
    return scaled_numbers