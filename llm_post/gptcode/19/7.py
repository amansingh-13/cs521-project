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

    # Split the input string into individual numberals
    numberals = numbers.split()

    # Convert the numberals to their corresponding numeric values using the dictionary
    numeric_values = [number_dict[numberal] for numberal in numberals]

    # Sort the numeric values
    sorted_numeric_values = sorted(numeric_values)

    # Convert the sorted numeric values back to numberals using the dictionary
    sorted_numberals = [list(number_dict.keys())[list(number_dict.values()).index(numeric_value)] for numeric_value in sorted_numeric_values]

    # Join the sorted numberals into a space-delimited string
    sorted_numbers = ' '.join(sorted_numberals)

    return sorted_numbers