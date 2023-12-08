def sort_numbers(numbers: str) -> str:
    # Convert the input string into a list of numbers
    number_list = numbers.split()
    
    # Create a dictionary to store the numerical value of each numberal
    number_values = {
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
    
    # Sort the number list based on the numerical values
    number_list.sort(key=lambda x: number_values[x])
    
    # Convert the sorted number list back into a string
    sorted_numbers = ' '.join(number_list)
    
    return sorted_numbers