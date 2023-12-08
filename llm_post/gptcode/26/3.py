def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    """
    unique_numbers = []
    for number in numbers:
        if numbers.count(number) == 1:
            unique_numbers.append(number)
    return unique_numbers