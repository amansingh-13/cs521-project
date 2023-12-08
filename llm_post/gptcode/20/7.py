def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    numbers.sort()

    # Initialize variables to track the closest numbers
    closest_diff = float('inf')
    closest_nums = None

    # Iterate through the sorted numbers and check the difference between adjacent pairs
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]

        # If the difference is smaller than the currently tracked closest difference,
        # update the closest difference and closest numbers
        if diff < closest_diff:
            closest_diff = diff
            closest_nums = (numbers[i], numbers[i+1])

    return closest_nums