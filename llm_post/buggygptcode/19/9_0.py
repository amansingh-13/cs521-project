def sort_numbers(numbers: str) -> str:
    # Create a dictionary to map numberals to their corresponding numbers
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
    
    # Convert each numberal to its corresponding number
    numbers = [number_dict[numberal] for numberal in numberals]
    
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Convert the sorted numbers back to numberals
    sorted_numberals = [numberal for number, numberal in sorted(number_dict.items(), key=lambda x: x[1]) if number in sorted_numbers]
    
    # Join the sorted numberals into a single string
    sorted_string = ' '.join(sorted_numberals)
    
    return sorted_string