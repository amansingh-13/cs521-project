def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize variables to store the closest elements
    closest_elements = (numbers[0], numbers[1])
    min_difference = numbers[1] - numbers[0]

    # Iterate through the list or update the closest elements if a smaller difference is found
    for i in range(1, len(numbers) - 1):
        difference = numbers[i+1] - numbers[i]
        if difference < min_difference:
            min_difference = difference
            closest_elements = (numbers[i], numbers[i+1])

    return closest_elements