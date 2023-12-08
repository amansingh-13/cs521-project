def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Iterate over each number in the list
    for i in range(len(numbers)):
        # Check if the difference between the current number and any other number in the list is less than the threshold
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False