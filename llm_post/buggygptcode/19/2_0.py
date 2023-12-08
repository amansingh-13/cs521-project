def sort_numbers(numbers: str) -> str:
    # Create a dictionary to map numberals to their corresponding numeric values
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
    
    # Split the input string into a list of numberals
    numberals = numbers.split()
    
    # Convert the numberals to numeric values using the number_dict
    numeric_values = [number_dict[numeral] for numeral in numberals]
    
    # Sort the numeric values in ascending order
    sorted_values = sorted(numeric_values)
    
    # Convert the sorted numeric values back to numberals using the number_dict
    sorted_numberals = [key for value in sorted_values for key, val in number_dict.items() if val == value]
    
    # Join the sorted numberals into a string with space delimiter
    sorted_numbers = ' '.join(sorted_numberals)
    
    return sorted_numbers