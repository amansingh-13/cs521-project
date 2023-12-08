def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 or the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    rescaled_numbers = []
    for num in numbers:
        rescaled_num = (num - min_num) / (max_num - min_num)
        rescaled_numbers.append(rescaled_num)
    return rescaled_numbers