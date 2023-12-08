def change_base(x: int, base: int):
    # Create an empty list to store the digits of the converted number
    digits = []
    
    # Continue dividing x by base until x becomes 0
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        
        # Add the remainder to the list of digits
        digits.append(str(remainder))
        
        # Update x to be x divided by base (integer division)
        x = x // base
    
    # Reverse the list of digits and join them into a string
    return ''.join(digits[::-1])