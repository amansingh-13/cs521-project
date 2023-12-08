def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    min_num = min(numbers)
    max_num = max(numbers)
    rescaled_numbers = []
    for num in numbers:
        rescaled_num = (num - min_num) / (max_num - min_num)
        rescaled_numbers.append(rescaled_num)
    return rescaled_numbers