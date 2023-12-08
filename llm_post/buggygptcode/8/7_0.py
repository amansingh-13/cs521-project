def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize sum or product variables to 0 or 1 respectively
    sum_val = 0
    product_val = 1
    
    # Iterate through the numbers or update sum or product variables accordingly
    for num in numbers:
        sum_val += num
        product_val *= num
    
    # Return the sum or product as a tuple
    return sum_val, product_val