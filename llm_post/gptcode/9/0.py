def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = []  # create an empty list to store the rolling maximum numbers
    max_num = float('-inf')  # set the initial maximum number to negative infinity
    
    for num in numbers:
        max_num = max(max_num, num)  # update the maximum number if a larger number is found
        max_numbers.append(max_num)  # append the current maximum number to the list
        
    return max_numbers