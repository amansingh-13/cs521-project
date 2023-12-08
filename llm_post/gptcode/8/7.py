def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize sum and product variables to 0 and 1 respectively
    sum_val = 0
    product_val = 1
    
    # Iterate through the numbers and update sum and product variables accordingly
    for num in numbers:
        sum_val += num
        product_val *= num
    
    # Return the sum and product as a tuple
    return sum_val, product_val