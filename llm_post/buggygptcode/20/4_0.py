def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize variables to store the closest elements and their difference
    closest_elements = (numbers[0], numbers[1])
    min_difference = numbers[1] - numbers[0]

    # Iterate through the list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]

        # If the difference is smaller than the minimum difference, update the closest elements
        if difference < min_difference:
            closest_elements = (numbers[i], numbers[i + 1])
            min_difference = difference

    # Return the closest elements
    return closest_elements