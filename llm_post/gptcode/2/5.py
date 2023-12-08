def truncate_number(number: float) -> float:
    # Convert the number to a string
    number_str = str(number)
    
    # Find the index of the decimal point
    decimal_index = number_str.index('.')
    
    # Extract the decimal part of the number
    decimal_part = number_str[decimal_index + 1:]
    
    # Convert the decimal part back to a float
    decimal_part_float = float(decimal_part)
    
    return decimal_part_float