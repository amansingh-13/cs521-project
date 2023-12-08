def sort_numbers(numbers: str) -> str:
    # Create a dictionary to map numberals to their numerical value
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
    
    # Split the string by spaces and convert each numberal to its numerical value
    num_list = [number_dict[num] for num in numbers.split()]
    
    # Sort the numerical values
    sorted_nums = sorted(num_list)
    
    # Convert the sorted numerical values back to numberals
    sorted_numbers = [key for key, value in number_dict.items() if value in sorted_nums]
    
    # Join the sorted numberals into a string with spaces between them
    sorted_string = ' '.join(sorted_numbers)
    
    return sorted_string