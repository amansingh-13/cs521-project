def sort_numbers(numbers: str) -> str:
    # Create a mapping of numberals to their corresponding numerical values
    mapping = {
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
    
    # Convert each numberal to its corresponding numerical value
    numbers = [mapping[numberal] for numberal in numberals]
    
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Convert the numbers back to numberals
    sorted_numberals = [numberals[number] for number in numbers]
    
    # Join the sorted numberals into a string, separated by spaces
    return ' '.join(sorted_numberals)