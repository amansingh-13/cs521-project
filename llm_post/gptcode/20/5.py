def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # Sort the numbers in ascending order
    min_diff = float('inf')  # Initialize the minimum difference between two numbers to infinity
    closest_nums = ()  # Initialize an empty tuple to store the closest numbers

    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # Calculate the difference between two adjacent numbers

        if diff < min_diff:
            min_diff = diff
            closest_nums = (numbers[i], numbers[i+1])

    return closest_nums