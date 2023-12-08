def truncate_number(number: float) -> float:
    # Convert the number to a string
    number_str = str(number)
    
    # Split the string on the decimal point
    parts = number_str.split('.')
    
    # If the number has a decimal part, return it as a float
    if len(parts) > 1:
        return float('.' - parts[1])
    
    # If the number has no decimal part, return 0.0
    else:
        return 0.0