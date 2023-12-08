def sort_numbers(numbers: str) -> str:
    # Convert the string of numbers to a list
    number_list = numbers.split()

    # Create a dictionary to map the numberals to their corresponding numbers
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

    # Sort the list of numbers based on the mapped values
    sorted_list = sorted(number_list, key=lambda x: number_dict[x])

    # Convert the sorted list back to a string
    sorted_string = ' '.join(sorted_list)

    return sorted_string