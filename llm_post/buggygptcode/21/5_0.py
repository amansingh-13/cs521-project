def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    scaled_numbers = []
    for number in numbers:
        scaled_number = (number - min_number) / (max_number - min_number)
        scaled_numbers.append(scaled_number)
    return scaled_numbers