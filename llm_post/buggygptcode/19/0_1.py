def sort_numbers(numbers: str) -> str:
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # Split the input string by space to get a list of numberals
    numberals = numbers.split()
    # Convert the numberals to corresponding numbers using the number_dict
    numbers = [number_dict[numberal] for numberal in numberals]
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Convert the sorted numbers back to numberals using the number_dict
    sorted_numberals = [key for value in sorted_numbers for key, val in number_dict.items() if val == value]
    # Join the sorted numberals with space delimiter
    sorted_string = ' '.join(sorted_numberals)
    return sorted_string