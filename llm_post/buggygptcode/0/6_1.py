def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Iterate through each number in the list
    for i in range(len(numbers)):
        # Compare the current number with all the numbers after it
        for j in range(i + 1, len(numbers)):
            # If the absolute difference between the two numbers is less than the threshold, return True
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    # If no two numbers are closer to each other than the threshold, return False
    return False